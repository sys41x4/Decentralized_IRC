from ast import In
from ctypes import addressof
from logging import exception
import os, random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from api.models import api
import hashlib
# from user.models import user
import json
import psycopg2


msg_status = {0:'FAILED', 1:'SUCCESS'}
color = {0:'#e74c3c', 1:'#2ecc71'}

# Connect database for fetching
db_host = 'localhost'
db_port = 4321
# db_host = '172.17.0.3'
# db_port = 5432
# # docker postgres_container-port[5432](db_host=IP_of_Docker_Container) <----> Host Machine linked port [4321](db_host=localhost)
db_user = 'postgres'
db_pass = 'HelloWorld'
db_name = 'irc_project_data'

connect_str = f"host='{db_host}' port='{db_port}' dbname='{db_name}' user='{db_user}' password='{db_pass}'"

# use our connection values to establish a connection
conn = psycopg2.connect(connect_str)


# create a psycopg2 cursor that can execute queries
cursor = conn.cursor()


def gen_room_name(num):
    hash_list = []
    for i in range(num):
        hash_list+=list(hashlib.md5(os.urandom(128)+os.urandom(128)).hexdigest())
    
    random.shuffle(hash_list)
    
    return ''.join(hash_list)

# # Used during creation of new dm/group
# # will Be used Later on
# new_room = gen_room_name(2)


def get_uuid(wallet_address, network_id):
    cursor.execute(f"""SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' 
    AND user_connected_Wallets.networkid={network_id}""")
        
    uuid = cursor.fetchall()[0][0] # uuid from current_fetcher_Wallet_Address
    conn.commit()

    return uuid

def basic_usrData(wallet_address, network_id):
    # print('basic_usrData', wallet_address, network_id)
    cursor.execute(f"""SELECT user_details.name, user_details.primary_wallet_address, user_connected_wallets.wallet_address 
    FROM user_details, user_connected_wallets 
    WHERE user_details.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' AND user_connected_Wallets.networkid={network_id}) 
    AND user_connected_Wallets.uuid=user_details.uuid;""")

    rows = cursor.fetchall()
    conn.commit()

    usr_basic_details = [rows[0][0], rows[0][1], []]
    usr_basic_details = {
        'basic_data':{
            'name': rows[0][0],
            'uuid': get_uuid(wallet_address, network_id),
            'primary_address': rows[0][1],
            'wallet_address': []
            }
        }

    for i in range(len(rows)):
        usr_basic_details['basic_data']['wallet_address']+=[rows[i][2]]
    usr_basic_details['basic_data']['wallet_address']=tuple(usr_basic_details['basic_data']['wallet_address'])

    # print(usr_basic_details, '\n\n')

    return usr_basic_details
    
def dm_rooms(wallet_address, network_id):

# Get One<--->One or dm Room Data
    
    cursor.execute(f"""SELECT group_relation.room, contact_details.name, contact_details.primary_wallet_address, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid 
    FROM group_relation, contact_details, contacts_connected_wallets 
    where group_relation.room_type='dm' 
    AND group_relation.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' AND user_connected_Wallets.networkid={network_id}) 
    AND contact_details.uuid=group_relation.uuid 
    AND contacts_connected_wallets.uuid=group_relation.uuid 
    AND CAST(group_relation.wallet_address AS INTEGER)=contacts_connected_wallets.contactid 
    AND contact_details.contactid=contacts_connected_wallets.contactid;""")

    rows = cursor.fetchall()
    conn.commit()
    # print(rows, '\n\n')

    # # Get DM room Names
    # # dm_rooms=[]
    # # for i in range(len(rows)):
    # #     dm_rooms+=[rows[i][0]]
    # # dm_rooms=tuple(set(dm_rooms))

    dm_rooms={'dm':{}}

    for i in range(len(rows)):
        if rows[i][0] not in dm_rooms['dm']:
            dm_rooms['dm'].update({
                rows[i][0]:{
                    rows[i][1]:{
                        'primary_address':[rows[i][2], rows[i][4]],
                        'wallet_address':[rows[i][3]]
                        }
                    }
                }
            )

        else:
            dm_rooms['dm'][rows[i][0]][rows[i][1]]['wallet_address']+=[rows[i][3]]
    # print(dm_rooms, '\n\n')
    return dm_rooms

def group_rooms(wallet_address, network_id):

    # Group rooms one<--->many

    cursor.execute(f"""SELECT group_relation.room 
    FROM group_relation
    WHERE group_relation.room_type='group' 
    AND group_relation.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' AND user_connected_Wallets.networkid={network_id}) 
    ;""")

    rows = cursor.fetchall()
    conn.commit()

    total_group_rooms_query = str(rows)[1:-1].replace(')','').replace(',','').replace('(', 'OR group_relation.room=')[3:]
    # print(total_group_rooms_query, '\n\n')

    cursor.execute(f"""SELECT group_relation.room, group_relation.name, group_relation.wallet_address, user_connected_wallets.networkid 
    FROM group_relation, user_connected_wallets
    WHERE ({total_group_rooms_query})
    AND user_connected_wallets.wallet_address=group_relation.wallet_address;""")

    rows = cursor.fetchall()
    # print(rows, '\n\n')

    group_rooms={'group':{}}
    
    for i in range(len(rows)):
        if rows[i][0] not in group_rooms['group']:
            group_rooms['group'].update({
                rows[i][0]:{
                    rows[i][1]:{
                        'primary_address':[rows[i][2], rows[i][3]]
                        }
                    }
                }
            )

        else:
            group_rooms['group'][rows[i][0]].update({rows[i][1]:{'primary_address':[rows[i][2], rows[i][3]]}})
    # print(group_rooms, '\n\n')
    return group_rooms

def contacts(wallet_address, network_id):
    # Fetch All Contact Details
    cursor.execute(f"""SELECT contact_details.contactid, contact_details.name, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid 
    FROM contact_details, contacts_connected_wallets 
    WHERE contact_details.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' AND user_connected_Wallets.networkid={network_id}) 
    AND contacts_connected_wallets.uuid=contact_details.uuid 
    AND contacts_connected_wallets.contactid=contact_details.contactid;""")

    rows = cursor.fetchall()
    conn.commit()

    # all_contact_details = []
    contact_details = {'contacts':{}}
    for i in range(len(rows)):
        
        if rows[i][0] not in contact_details['contacts']:
            contact_details['contacts'].update({rows[i][0]:{rows[i][1]: [(rows[i][2], rows[i][3])]}})
        else:
            contact_details['contacts'][rows[i][0]][rows[i][1]]+=[(rows[i][2], rows[i][3])]
    
    # print(contact_details, '\n\n')
    return contact_details

def individual_contact(wallet_address, network_id, contact_wallet):
    # Fetch Individual Contact Detail
    cursor.execute(f"""SELECT contact_details.contactid, contact_details.name, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid 
    FROM contact_details, contacts_connected_wallets 
    WHERE contact_details.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' AND user_connected_Wallets.networkid={network_id}) 
    AND contacts_connected_wallets.uuid=contact_details.uuid 
    AND contacts_connected_wallets.contactid=(SELECT contacts_connected_wallets.contactid from contacts_connected_wallets where contacts_connected_wallets.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_address}' AND user_connected_Wallets.networkid={network_id}) AND contacts_connected_wallets.wallet_address='{contact_wallet}') 
    AND contacts_connected_wallets.contactid=contact_details.contactid;""")

    rows = cursor.fetchall()
    conn.commit()

    indv_contact = {'contact':{}}

    for i in range(len(rows)):
        if rows[i][0] not in indv_contact['contact']:
            indv_contact['contact'].update({rows[i][0]:{rows[i][1]:[(rows[i][2], rows[i][3])]}})
        else:
            indv_contact['contact'][rows[i][0]][rows[i][1]]+=[(rows[i][2], rows[i][3])]

    # print(indv_contact, '\n\n')
    return indv_contact

def communication_data(wallet_address, network_id, room_type, room=0):

    basicUsrData = basic_usrData(wallet_address, network_id)['basic_data']

    # room_type ='individual'/'dm'/'group'/'all'
    # For room_type='individual', Room_Name->room is to be mentioned
    get_room_list_subquery=''
    if room_type!='all':get_room_list_subquery="group_relation.room_type='{room_type}' AND "
    
    if room_type=='individual':
        total_group_rooms_query = "communication_data.room='{room}'"
    else:
        cursor.execute(f"""SELECT group_relation.room 
        FROM group_relation
        WHERE {get_room_list_subquery}
        group_relation.uuid='{basicUsrData['uuid']}'
        ;""")

        rows = cursor.fetchall()
        conn.commit()

        total_group_rooms_query = str(rows)[1:-1].replace(')','').replace(',','').replace('(', 'OR communication_data.room=')[3:]
    # print(total_group_rooms_query, '\n\n')
    
    cursor.execute(f"""SELECT communication_data.room, communication_data.sender, communication_data.timestamp, communication_data.msgdata, communication_data.room_type 
    FROM communication_data
    WHERE {total_group_rooms_query} ORDER BY communication_data.timestamp;""")

    rows = cursor.fetchall()
    conn.commit()

    # print(rows, '\n\n')


    comm_data = {'communication_data':{}}
    for i in range(len(rows)):

        if rows[i][4]=='dm':
            if rows[i][1]==basicUsrData['uuid']:
                sender='you'
            else:
                sender='contact'
        else:
            if rows[i][1] in basicUsrData['wallet_address']:
                sender='you'
            else:
                sender=rows[i][1]


        if rows[i][4] not in comm_data['communication_data']:
            comm_data['communication_data'].update({

                rows[i][4]:{
                    rows[i][0]:{
                        sender:{
                            rows[i][2]:{
                                'data': rows[i][3]
                            }
                        }
                    }
                }
            })
        else:

            if rows[i][0] not in comm_data['communication_data'][rows[i][4]]:

                comm_data['communication_data'][rows[i][4]].update({
                    rows[i][0]:{
                        sender:{
                            rows[i][2]:{
                                'data': rows[i][3]
                            }
                        }
                    }
                })
            
            else:

                if sender not in comm_data['communication_data'][rows[i][4]][rows[i][0]]:
                    comm_data['communication_data'][rows[i][4]][rows[i][0]].update({
                        sender:{
                            rows[i][2]:{
                                'data': rows[i][3]
                            }
                        }
                    })

                else:

                    comm_data['communication_data'][rows[i][4]][rows[i][0]][sender].update({
                        rows[i][2]:{
                            'data': rows[i][3]
                        }
                    })

    # print(comm_data, '\n\n')
    return comm_data

def insert_communication_data(communication_data):
    #{ 'room_type': contact_details['room_type'],
	# 	'room': contact_details['room'],
	# 	'sender': ethereum.selectedAddress.toUpperCase(),
	# 	'receiver': contact_details['rcvr_wallet_addresses'],
	# 	'message': message,
    #   'timestamp': timestamp,}

    cursor.execute(f"""SELECT COUNT(room) FROM group_relation WHERE room='{communication_data['room']}';""")
    room_count = cursor.fetchall()[0][0]
    print(room_count)
    conn.commit()

    if room_count>0:
        values = f"""('{communication_data['room']}', 
        '{communication_data['room_type']}', 
        (SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{communication_data['sender']}'), 
        '{communication_data['message']}', 
        {communication_data['timestamp']});"""
        
        cursor.execute(f"""INSERT INTO communication_data (room, room_type, sender, msgData, timestamp) VALUES """+values)
        conn.commit()
    
        return {'msg_status': 'SUCCESS', 'color': '#2ecc71', 'output': 'Message Sent Successfully'}
    else:
        return {'msg_status': 'FAILED', 'color': '#e74c3c', 'output': 'User Request is corrupted', 'message_data': []}

@csrf_protect
def startup_data(request):
    if request.method == "POST":
        try:
        # Parameters
        # # Fetcher:
        # ('self', 'current_WalletAddress')
        # 


            data = json.loads(request.body)
            wallet_address = data['current_WalletAddress']
            network_id = int(data['network_id'])

            startupData = {
                'startup_data':{
                    'basic_data':basic_usrData(wallet_address, network_id)['basic_data'],
                    'rooms':{
                        'dm':dm_rooms(wallet_address, network_id)['dm'],
                        'group':group_rooms(wallet_address, network_id)['group'],
                    },
                    'communication_data':communication_data(wallet_address, network_id, 'all')['communication_data'],
                }}
            # print(startupData)
            return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': 'Startup Data fetched Successfully', 'data':startupData})
            
        except:
                output = "An ERROR occured\nStartup Data not fetched Successfully"
                # print(output)
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})

