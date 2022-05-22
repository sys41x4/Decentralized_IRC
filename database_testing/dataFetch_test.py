# postgres://<db_user>:<db_password>@<db_host>:<port>/<db_name>
import sys
import os
import subprocess
# For DataBase Storage
import psycopg2

uuid_linked_walletAddr, basic_user_detail, contact_details, communication_data, group_room_data = 0, 0, 0, 0, 0
def load_data():
    global uuid_linked_walletAddr, basic_user_detail, contact_details, communication_data, group_room_data

    uuid_linked_walletAddr={
        '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9':{'uuid':'863dc52a-c39c-11ec-8b20-82304926de9b', 'networkId':42},
        '0X283C3B6A4D84D457F1B6BB8FB947CFA432EFC293':{'uuid':'863dc52a-c39c-11ec-8b20-82304926de9b', 'networkId':42},
        '0XFFE39E1461D0361C3D72658EF39AE76288C82622':{'uuid':'a149137f-c39b-11ec-81f4-82304926de9b', 'networkId':42},
        '0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9':{'uuid':'a149137f-c39b-11ec-81f4-82304926de9b', 'networkId':42},
        '0X68237960F18F2B3A1555A39CD3427C52B98AD10B':{'uuid':'6905735c-c511-11ec-a9f3-82304926de9b', 'networkId':42},
        '0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B':{'uuid':'5fa6aee8-cf80-11ec-9735-82304926de9b', 'networkId':42},

    }


    basic_user_detail = {
        '863dc52a-c39c-11ec-8b20-82304926de9b': {
            'name':'Arijit Bhowmick',
            'totalContacts':3,
            'primary_wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
            'connected_wallets':[
                {
                    'wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                    'networkId':42,
                },

                {
                    'wallet_address':'0X283C3B6A4D84D457F1B6BB8FB947CFA432EFC293',
                    'networkId':42,
                },
            ]

        },

        'a149137f-c39b-11ec-81f4-82304926de9b': {
            'name':'sys41x4',
            'totalContacts':1,
            'primary_wallet_address':'0XFFE39E1461D0361C3D72658EF39AE76288C82622',
            'connected_wallets':[
                {
                    'wallet_address':'0XFFE39E1461D0361C3D72658EF39AE76288C82622',
                    'networkId':42,
                },

                {
                    'wallet_address':'0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9',
                    'networkId':42,
                },
            ]
        },

        '6905735c-c511-11ec-a9f3-82304926de9b': {
            'name':'Suraj Disoja',
            'totalContacts':3,
            'primary_wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
            'connected_wallets':[
                {
                    'wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                    'networkId':42,
                }
            ]
        },

        '5fa6aee8-cf80-11ec-9735-82304926de9b' : {
            'name':'ninetyn1ne',
            'totalContacts':2,
            'primary_wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
            'connected_wallets':[
                {
                    'wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
                    'networkId':42,
                }
            ]
        },
    }

    contact_details = {
        '863dc52a-c39c-11ec-8b20-82304926de9b': {
            'contactsList':{
                0:{
                    'name': 'sys41x4',
                    'primary_wallet_address':'0XFFE39E1461D0361C3D72658EF39AE76288C82622',
                    'walletList':[
                        {
                            'wallet_address':'0XFFE39E1461D0361C3D72658EF39AE76288C82622',
                            'networkId':42,
                        },

                        {
                            'wallet_address':'0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9',
                            'networkId':42,
                        }
                        
                    ]
                },

                1:{
                    'name': 'Suraj Disoja',
                    'primary_wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                    'walletList':[
                        {
                            'wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                            'networkId':42,
                        }

                    ]
                },

                2:{
                    'name': 'ninetyn1ne',
                    'primary_wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
                    'walletList':[
                        {
                            'wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
                            'networkId':42,
                        }

                    ]
                }
            },
        },

        'a149137f-c39b-11ec-81f4-82304926de9b': {
            'contactsList':{
                0:{
                    'name': 'Arijit Bhowmick',
                    'primary_wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                    'walletList':[
                        {
                            'wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                            'networkId':42,
                        }
                    ]
                },

                1:{
                    'name': 'Suraj Disoja',
                    'primary_wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                    'walletList':[
                        {
                            'wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                            'networkId':42,
                        }

                    ]
                }
            },
        },
            
        '6905735c-c511-11ec-a9f3-82304926de9b': {
            'contactsList':{
                0:{
                    'name': 'Arijit Bhowmick',
                    'primary_wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                    'walletList':[
                        {
                            'wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                            'networkId':42,
                        }
                    ]
                },

                1:{
                    'name': 'sys41x4',
                    'primary_wallet_address':'0XFFE39E1461D0361C3D72658EF39AE76288C82622',
                    'walletList':[
                        {
                            'wallet_address':'0XFFE39E1461D0361C3D72658EF39AE76288C82622',
                            'networkId':42,
                        }
                    ]
                },

                2:{
                    'name': 'ninetyn1ne',
                    'primary_wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
                    'walletList':[
                        {
                            'wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
                            'networkId':42,
                        }
                    ]
                }
            },

        },

        '5fa6aee8-cf80-11ec-9735-82304926de9b': {
            'contactsList':{
                0:{
                    'name': 'Arijit Bhowmick',
                    'primary_wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                    'walletList':[
                        {
                            'wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                            'networkId':42,
                        }
                    ]
                },

                1:{
                    'name': 'Suraj Disoja',
                    'primary_wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                    'walletList':[
                        {
                            'wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                            'networkId':42,
                        }

                    ]
                }
            },

        },
    }

    group_room_data = {
        '0315c67d2abd831a0e3cb5bf1b1393cf8dfe3df298964ef66b96ac2194c19504':{
            'type':'dm',
            '863dc52a-c39c-11ec-8b20-82304926de9b':['','0'],
            'a149137f-c39b-11ec-81f4-82304926de9b':['','0'],

        },

        'd39ae179061b256be35f6feea91d5a6633e493e4850711c45b07607d0f5e5b27':{
            'type':'dm',
            '863dc52a-c39c-11ec-8b20-82304926de9b':['','1'],
            '6905735c-c511-11ec-a9f3-82304926de9b':['','0'],
        },

        '9c44edb59f25db1aba4bc8d86b6ca88049145265a4c37652ad86c9e0ffe46a66':{
            'type':'dm',
            '863dc52a-c39c-11ec-8b20-82304926de9b':['','2'],
            '5fa6aee8-cf80-11ec-9735-82304926de9b':['','0'],
        },

        '833185119a147a088bd7ef322dfea6caf6080a50a1e07c020a6007c999721ecd':{
            'type':'dm',
            '6905735c-c511-11ec-a9f3-82304926de9b':['','1'],
            'a149137f-c39b-11ec-81f4-82304926de9b':['','1'],
        },

        '1f5eb015e712c32033dd465de4e45fa1d516870af9d153b2c73a3157c007738e':{
            'type':'dm',
            '6905735c-c511-11ec-a9f3-82304926de9b':['','2'],
            '5fa6aee8-cf80-11ec-9735-82304926de9b':['','1'],
        },




        'f28b351c9d30d37ebc3a2cb7adc71873eec3217c3e5b86450eb0c0280be95d6f':{
            'type':'group',
            '863dc52a-c39c-11ec-8b20-82304926de9b':['Arijit BHowmick 1', '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9'],
            'a149137f-c39b-11ec-81f4-82304926de9b':['sys41x4 1', '0XFFE39E1461D0361C3D72658EF39AE76288C82622'],
            '6905735c-c511-11ec-a9f3-82304926de9b':['Suraj Disoja 1', '0X68237960F18F2B3A1555A39CD3427C52B98AD10B'],
            '5fa6aee8-cf80-11ec-9735-82304926de9b':['ninetyn1ne 1', '0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B'],
        },

        '2977ed9e347c52bc69533574122c13d18fa3137e622c274c4aade632d6f71801':{
            '863dc52a-c39c-11ec-8b20-82304926de9b':['Arijit BHowmick 2', '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9'],
            'a149137f-c39b-11ec-81f4-82304926de9b':['sys41x4 2', '0XFFE39E1461D0361C3D72658EF39AE76288C82622'],
            '6905735c-c511-11ec-a9f3-82304926de9b':['Suraj Disoja 2', '0X68237960F18F2B3A1555A39CD3427C52B98AD10B'],
        },

        '3143876504ca0ffe638dc21814bff8899ac654f0d596ab93f36783ea8c48acc1':{
            'type':'group',
            'a149137f-c39b-11ec-81f4-82304926de9b':['sys41x4 3', '0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9'],
            '863dc52a-c39c-11ec-8b20-82304926de9b':['Arijit BHowmick 3', '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9'],
        },

        '763e08c99455f5323234aa3a23a087d84d89e781bfa56a41b06a80f32ab0155a':{
            'type':'group',
            '6905735c-c511-11ec-a9f3-82304926de9b':['Suraj Disoja 3', '0X68237960F18F2B3A1555A39CD3427C52B98AD10B'],
            '863dc52a-c39c-11ec-8b20-82304926de9b':['Arijit BHowmick 4', '0X283C3B6A4D84D457F1B6BB8FB947CFA432EFC293'],
            'a149137f-c39b-11ec-81f4-82304926de9b':['sys41x4 4', '0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9'],
            '5fa6aee8-cf80-11ec-9735-82304926de9b':['ninetyn1ne 2', '0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B'],
        },

        '5e4cef1f93ef1376b1451a8eb2cbc3eca4c79b572915b6e9a38c99f351243b09':{
            'type':'group',
            '5fa6aee8-cf80-11ec-9735-82304926de9b':['ninetyn1ne 3', '0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B'],
            '863dc52a-c39c-11ec-8b20-82304926de9b':['Arijit BHowmick 5', '0X283C3B6A4D84D457F1B6BB8FB947CFA432EFC293'],
            '6905735c-c511-11ec-a9f3-82304926de9b':['Suraj Disoja 4', '0X68237960F18F2B3A1555A39CD3427C52B98AD10B'],
        },
    }

    # communication_data = {

    #     '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9-0XFFE39E1461D0361C3D72658EF39AE76288C82622':{
    #         1650707120.936152: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':0, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'contactID':0, 'message':'Hello Man Whats Up', 'networkId':42, 'timestamp':1650707120.936152},
    #         1650707282.4517663: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':1, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'contactID':0, 'message':'What\'s going on ?', 'networkId':42, 'timestamp':1650707282.4517663},
    #         1650707328.6830337: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':2, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'contactID':0, 'message':'I am just watching a movie...', 'networkId':42, 'timestamp':1650707328.6830337},
    #         1650707338.0125976: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':3, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'contactID':0, 'message':'Hey Man Are You Still there ?', 'networkId':42, 'timestamp':1650707338.0125976},
    #         1650707348.8427203: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':4, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'contactID':0, 'message':'Mannn.. Again you are offline ... -_- ', 'networkId':42, 'timestamp':1650707348.8427203},
    #         1650707156.6189778: {'sender':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'nonce':0, 'receiver':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'contactID':0, 'message':'I am good what\'s you doing ? ', 'networkId':42, 'timestamp':1650707156.6189778},
    #         1650707290.8573165: {'sender':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'nonce':1, 'receiver':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'contactID':0, 'message':'Nothing much, Just chilling with laptop', 'networkId':42, 'timestamp':1650707290.8573165},
    #     },
        
        
    # }

    communication_data = {

        '0315c67d2abd831a0e3cb5bf1b1393cf8dfe3df298964ef66b96ac2194c19504':{
            'type':'dm',
            'msg_data':{
                1650707120.936152: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':0, 'message':'Hello Man Whats Up', 'timestamp':1650707120.936152},
                1650707282.4517663: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':1, 'message':'What\'s going on ?', 'timestamp':1650707282.4517663},
                1650707328.6830337: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':2, 'message':'I am just watching a movie...', 'timestamp':1650707328.6830337},
                1650707338.0125976: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':3, 'message':'Hey Man Are You Still there ?', 'timestamp':1650707338.0125976},
                1650707348.8427203: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':4, 'message':'Mannn.. Again you are offline ... -_- ', 'timestamp':1650707348.8427203},
                1650707156.6189778: {'sender':'a149137f-c39b-11ec-81f4-82304926de9b', 'nonce':0, 'message':'I am good what\'s you doing ? ', 'timestamp':1650707156.6189778},
                1650707290.8573165: {'sender':'a149137f-c39b-11ec-81f4-82304926de9b', 'nonce':1, 'message':'Nothing much, Just chilling with laptop', 'timestamp':1650707290.8573165},
            }
            
        },
        
        
    }


db_host = 'localhost'
db_port = 4321
# db_host = '172.17.0.3'
# db_port = 5432
# # docker postgres_container-port[5432](db_host=IP_of_Docker_Container) <----> Host Machine linked port [4321](db_host=localhost)
db_user = 'postgres'
db_pass = 'HelloWorld'
db_name = 'irc_project_data'
# storage_location = sys.argv[6]

# db_name = sys.argv[1]
do = sys.argv[1]
# do = sys.argv[2]

# do = 'createDB'
# do = 'createTable'
# do = 'insert'
# do = 'fetch'
# Create DataBase and Required Tables

try:
    # Create New database [On First run]
    connect_str = f"host='{db_host}' port='{db_port}' dbname='{db_name}' user='{db_user}' password='{db_pass}'"
    
    # # Execute Commands on already Created Databases
    if do=='createDB':
        connect_str = f"host='{db_host}' port='{db_port}' user='{db_user}' password='{db_pass}'"

    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)

    if do=='createDB':conn.autocommit = True

    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    if do=='createDB':
        
        # Create New DB
        cursor.execute(f"""CREATE DATABASE {db_name};""")

    elif do=='createTable':
        # create a new table with a 3 column called "uuid", "name" and "primary_wallet_address"
        cursor.execute("""CREATE TABLE user_details (uuid varchar, name varchar, primary_wallet_address varchar, totalContacts varchar);""")

        # create a new table with a 3 column called "uuid", "wallet_address" and "networkId"
        cursor.execute("""CREATE TABLE user_connected_wallets (uuid varchar, wallet_address varchar, networkId integer);""")

        # create a new table with a 4 column called "uuid", "id", "name", and "primary_wallet_address"
        # cursor.execute("""CREATE TABLE contact_details (uuid varchar, contactID integer, name varchar, primary_wallet_address varchar, room varchar);""")
        cursor.execute("""CREATE TABLE contact_details (uuid varchar, contactID integer, name varchar, primary_wallet_address varchar);""")

        # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
        cursor.execute("""CREATE TABLE contacts_connected_wallets (uuid varchar, contactID integer, wallet_address varchar, networkId integer);""")
        # cursor.execute("""CREATE TABLE contacts_connected_wallets (uuid varchar, contactID integer, wallet_address text[][], networkId integer[]);""")

    #         communication_data = {

    #     '0315c67d2abd831a0e3cb5bf1b1393cf8dfe3df298964ef66b96ac2194c19504':{
    #         'type':'dm',
    #         1650707120.936152: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':0, 'message':'Hello Man Whats Up', 'timestamp':1650707120.936152},
    #         1650707282.4517663: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':1, 'message':'What\'s going on ?', 'timestamp':1650707282.4517663},
    #         1650707328.6830337: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':2, 'message':'I am just watching a movie...', 'timestamp':1650707328.6830337},
    #         1650707338.0125976: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':3, 'message':'Hey Man Are You Still there ?', 'timestamp':1650707338.0125976},
    #         1650707348.8427203: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':4, 'message':'Mannn.. Again you are offline ... -_- ', 'timestamp':1650707348.8427203},
    #         1650707156.6189778: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':0, 'message':'I am good what\'s you doing ? ', 'timestamp':1650707156.6189778},
    #         1650707290.8573165: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':1, 'message':'Nothing much, Just chilling with laptop', 'timestamp':1650707290.8573165},
    #     },
        
        
    # }

        # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
        # cursor.execute("""CREATE TABLE communication_data (uuid varchar, contactID integer, nonce integer, networkId integer, msgData varchar, timestamp float);""")
        cursor.execute("""CREATE TABLE communication_data (room varchar, room_type varchar, sender varchar, nonce integer, msgData varchar, timestamp float);""")

        # create a new table with a 2 column called "uuid", "room" and "Participants"
        # cursor.execute("""CREATE TABLE group_relation (uuid varchar, room varchar, contactIDs smallint[]);""")
        cursor.execute("""CREATE TABLE group_relation (room varchar, uuid varchar, name varchar, wallet_address varchar, room_type varchar);""")


    elif do=='insert':
        load_data()

        #     group_room_data = {
        # '863dc52a-c39c-11ec-8b20-82304926de9b':{
        #     'room': 'f28b351c9d30d37ebc3a2cb7adc71873eec3217c3e5b86450eb0c0280be95d6f',
        #     'contactIDs':[
        #         0,
        #         1,
        #         2,
        #     ]
        # },

        for wallet_addr in uuid_linked_walletAddr:
            # INSERT into table with a 3 column called "uuid", "wallet_address" and "networkId"
            values = f"""('{uuid_linked_walletAddr[wallet_addr]['uuid']}', '{wallet_addr}', {uuid_linked_walletAddr[wallet_addr]['networkId']});"""
            cursor.execute("""INSERT INTO user_connected_wallets (uuid, wallet_address, networkId) VALUES """+values)
            
        for uuid in basic_user_detail:
            # create a new table with a 3 column called "uuid", "name" and "primary_wallet_address"
            values = f"""('{uuid}', '{basic_user_detail[uuid]['name']}', '{basic_user_detail[uuid]['primary_wallet_address']}', {basic_user_detail[uuid]['totalContacts']});"""
            cursor.execute("""INSERT INTO user_details (uuid, name, primary_wallet_address, totalContacts) VALUES """+values)

        for uuid in contact_details:
            for contact_id in contact_details[uuid]['contactsList']:
                # create a new table with a 4 column called "uuid", "id", "name", and "primary_wallet_address"
                # values = f"""('{uuid}', {contact_id}, '{contact_details[uuid]['contactsList'][contact_id]['name']}', '{contact_details[uuid]['contactsList'][contact_id]['primary_wallet_address']}', '{contact_details[uuid]['contactsList'][contact_id]['room']}');"""
                # cursor.execute(f"""INSERT INTO contact_details (uuid, contactID, name, primary_wallet_address, room) VALUES """+values)
                values = f"""('{uuid}', {contact_id}, '{contact_details[uuid]['contactsList'][contact_id]['name']}', '{contact_details[uuid]['contactsList'][contact_id]['primary_wallet_address']}');"""
                cursor.execute(f"""INSERT INTO contact_details (uuid, contactID, name, primary_wallet_address) VALUES """+values)

                for walletDetail in range(len(contact_details[uuid]['contactsList'][contact_id]['walletList'])):
                    # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
                    values = f"""('{uuid}', {contact_id}, '{contact_details[uuid]['contactsList'][contact_id]['walletList'][walletDetail]['wallet_address']}', {contact_details[uuid]['contactsList'][contact_id]['walletList'][walletDetail]['networkId']});"""
                    # print(values)
                    cursor.execute(f"""INSERT INTO contacts_connected_wallets (uuid, contactID, wallet_address, networkId) VALUES """+values)
        # for uuid in contact_details:
        #     wallet_list=[]
        #     network_list=[]
        #     for contact_id in contact_details[uuid]['contactsList']:
        #         # create a new table with a 4 column called "uuid", "id", "name", and "primary_wallet_address"
        #         values = f"""('{uuid}', {contact_id}, '{contact_details[uuid]['contactsList'][contact_id]['name']}', '{contact_details[uuid]['contactsList'][contact_id]['primary_wallet_address']}', '{contact_details[uuid]['contactsList'][contact_id]['room']}');"""
        #         cursor.execute(f"""INSERT INTO contact_details (uuid, contactID, name, primary_wallet_address, room) VALUES """+values)

        #         for walletDetail in range(len(contact_details[uuid]['contactsList'][contact_id]['walletList'])):
        #             # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
        #             wallet_list+=[contact_details[uuid]['contactsList'][contact_id]['walletList'][walletDetail]['wallet_address']]
        #             network_list+=[contact_details[uuid]['contactsList'][contact_id]['walletList'][walletDetail]['networkId']]
        #         # values = f"""('{uuid}', {contact_id}, '{str(set(wallet_list)).replace("'",'"')}', '{{{str(network_list)[1:-1]}}}');"""
        #         values = f"""('{uuid}', {contact_id}, ARRAY{wallet_list}, ARRAY{network_list});"""

        #         # print(values)
                    
        #         cursor.execute(f"""INSERT INTO contacts_arrayed_connected_wallets (uuid, contactID, wallet_address, networkId) VALUES """+values)


        # for i in communication_data:
        #     for timestamp in sorted(communication_data[i]):
        #         uuid = uuid_linked_walletAddr[communication_data[i][timestamp]['sender']]['uuid']
        #         contact_id = communication_data[i][timestamp]['contactID']
        #         # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
        #         values = f"""('{uuid}', {communication_data[i][timestamp]['contactID']}, {communication_data[i][timestamp]['nonce']}, {communication_data[i][timestamp]['networkId']}, '{communication_data[i][timestamp]['message'].encode().hex()}', {timestamp});"""
        #         cursor.execute(f"""INSERT INTO communication_data (uuid, contactID, nonce, networkId, msgData, timestamp) VALUES """+values)

        #    '0315c67d2abd831a0e3cb5bf1b1393cf8dfe3df298964ef66b96ac2194c19504':{
    #         'type':'dm',
    #         1650707120.936152: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':0, 'message':'Hello Man Whats Up', 'timestamp':1650707120.936152},
    #         1650707282.4517663: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':1, 'message':'What\'s going on ?', 'timestamp':1650707282.4517663},
    #         1650707328.6830337: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':2, 'message':'I am just watching a movie...', 'timestamp':1650707328.6830337},
    #         1650707338.0125976: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':3, 'message':'Hey Man Are You Still there ?', 'timestamp':1650707338.0125976},
    #         1650707348.8427203: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':4, 'message':'Mannn.. Again you are offline ... -_- ', 'timestamp':1650707348.8427203},
    #         1650707156.6189778: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':0, 'message':'I am good what\'s you doing ? ', 'timestamp':1650707156.6189778},
    #         1650707290.8573165: {'sender':'863dc52a-c39c-11ec-8b20-82304926de9b', 'nonce':1, 'message':'Nothing much, Just chilling with laptop', 'timestamp':1650707290.8573165},
    #     },
        
        
    # }

        # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
        # cursor.execute("""CREATE TABLE communication_data (uuid varchar, contactID integer, nonce integer, networkId integer, msgData varchar, timestamp float);""")
        # cursor.execute("""CREATE TABLE communication_data (room varchar, room_type varchar, sender varchar, nonce integer, msgData varchar, timestamp float);""")

        for room in communication_data:
            room_type = communication_data[room]['type']
            for timestamp in sorted(communication_data[room]['msg_data']):
                # if timestamp!='type':
                # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
                values = f"""('{room}', '{room_type}', '{communication_data[room]['msg_data'][timestamp]['sender']}', {communication_data[room]['msg_data'][timestamp]['nonce']}, '{communication_data[room]['msg_data'][timestamp]['message'].encode().hex()}', {communication_data[room]['msg_data'][timestamp]['timestamp']});"""
                cursor.execute(f"""INSERT INTO communication_data (room, room_type, sender, nonce, msgData, timestamp) VALUES """+values)

        # for i in communication_data:
        #     for timestamp in sorted(communication_data[i]):
        #         uuid = uuid_linked_walletAddr[communication_data[i][timestamp]['sender']]['uuid']
        #         contact_id = communication_data[i][timestamp]['contactID']
        #         # create a new table with a 4 column called "uuid", "id", "wallet_address" and "networkId"
        #         values = f"""('{uuid}', {communication_data[i][timestamp]['contactID']}, {communication_data[i][timestamp]['nonce']}, {communication_data[i][timestamp]['networkId']}, '{communication_data[i][timestamp]['message']}', {timestamp});"""
        #         cursor.execute(f"""INSERT INTO communication_data (uuid, room, nonce, networkId, msgData, timestamp) VALUES """+values)


        # for room in group_room_data:
        #     for i in range(len(group_room_data[uuid])):
        #         values = f"""('{uuid}', '{group_room_data[uuid][i]['room']}', '{set(group_room_data[uuid][i]['contactIDs'])}');"""
        #         cursor.execute(f"""INSERT INTO group_relation (uuid, room, contactIDs) VALUES """+values)        
        
        # group_relation_data = []
        # for room in group_room_data:
        #     for uuid in group_room_data[room]:
        #         if uuid=='type':
        #             roomType=group_room_data[room][uuid]
        #         else:
        #             group_relation_data+=[(room, uuid, group_room_data[room][uuid], roomType)]
        #         values = f"""{str(group_relation_data)[1:-1]};"""
        # cursor.execute(f"""INSERT INTO group_relation (room, uuid, wallet_address) VALUES """+values)
        group_relation_data = []
        for room in group_room_data:
            for uuid in group_room_data[room]:
                if uuid=='type':
                    roomType = group_room_data[room][uuid]
                else:
                    group_relation_data+=[(room, uuid, group_room_data[room][uuid][0], group_room_data[room][uuid][1], roomType)]
                values = f"""{str(group_relation_data)[1:-1]};"""
        cursor.execute(f"""INSERT INTO group_relation (room, uuid, name, wallet_address, room_type) VALUES """+values)
        
    elif do=='fetch':

        usr_uuid = '863dc52a-c39c-11ec-8b20-82304926de9b'
        # uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_addr}' AND user_connected_Wallets.networkid={network_id})
        wallet_addr = '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9'
        rcvr_pmry_addr = '0XFFE39E1461D0361C3D72658EF39AE76288C82622'
        network_id = 42
        
        cursor.execute(f"""SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_addr}' 
        AND user_connected_Wallets.networkid={network_id}""")
        
        uuid = cursor.fetchall()[0][0] # uuid from current_fetcher_Wallet_Address

        cursor.execute(f"""SELECT user_details.name, user_details.primary_wallet_address, user_connected_wallets.wallet_address 
        FROM user_details, user_connected_wallets 
        WHERE user_details.uuid='{uuid}' 
        AND user_connected_Wallets.uuid=user_details.uuid;""")

        rows = cursor.fetchall()

        usr_basic_details = [rows[0][0], rows[0][1], []]
        usr_basic_details = {
            'basic_data':{
                'name': rows[0][0],
                'uuid': uuid,
                'primary_address': rows[0][1],
                'wallet_address': []
                }
            }

        for i in range(len(rows)):
            usr_basic_details['basic_data']['wallet_address']+=[rows[i][2]]
        usr_basic_details['basic_data']['wallet_address']=tuple(usr_basic_details['basic_data']['wallet_address'])

        print(usr_basic_details, '\n\n') # (User Full Name, Primary_Wallet_Addresses (Connected_Wallet Addresses))

        # # Fetch Contacts Detail
        cursor.execute(f"""SELECT contact_details.contactid, contact_details.name, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid  FROM contact_details, contacts_connected_wallets WHERE contact_details.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_addr}' AND user_connected_Wallets.networkid={network_id}) AND contacts_connected_wallets.uuid=contact_details.uuid AND contacts_connected_wallets.contactid=contact_details.contactid;""")
        rows = cursor.fetchall()

        # all_contact_details = []
        all_contact_details_dict = {'contacts':{}}
        for i in range(len(rows)):
            
            if rows[i][0] not in all_contact_details_dict['contacts']:
                all_contact_details_dict['contacts'].update({rows[i][0]:{rows[i][1]: [[rows[i][2], rows[i][3]]]}})
                # print(all_contact_details_dict)
            else:
                all_contact_details_dict['contacts'][rows[i][0]][rows[i][1]]+=[[rows[i][2], rows[i][3]]]
        
        print(all_contact_details_dict, '\n\n')

        # Fetch Individual Contact
        cursor.execute(f"""SELECT contact_details.contactid, contact_details.name, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid 
        FROM contact_details, contacts_connected_wallets 
        WHERE contact_details.uuid='{uuid}' 
        AND contacts_connected_wallets.uuid=contact_details.uuid 
        AND contacts_connected_wallets.contactid=(SELECT contacts_connected_wallets.contactid from contacts_connected_wallets where contacts_connected_wallets.uuid='{uuid}' AND contacts_connected_wallets.wallet_address='{rcvr_pmry_addr}') 
        AND contacts_connected_wallets.contactid=contact_details.contactid;""")

        rows = cursor.fetchall()
        # print(rows, '\n\n')

        indv_contact = {'contact':{}}

        for i in range(len(rows)):
            if rows[i][0] not in indv_contact['contact']:
                indv_contact['contact'].update({rows[i][0]:{rows[i][1]:[(rows[i][2], rows[i][3])]}})
            else:
                indv_contact['contact'][rows[i][0]][rows[i][1]]+=[(rows[i][2], rows[i][3])]

        print(indv_contact, '\n\n')
        # # print(all_contact_details_dict, '\n\n')
        # # Changing lists & dictionaries to tuples to reduce memory size usage
        # for contact_id in all_contact_details_dict:
        #     all_contact_details+=[(contact_id, all_contact_details_dict[contact_id][0], tuple(all_contact_details_dict[contact_id][1]))]
        # all_contact_details=tuple(all_contact_details)
        
        # print(all_contact_details)

        # # # Get One<--->One or dm Room Data
        # chat_ids=[]
        # cursor.execute(f"""SELECT contact_details.room, contact_details.name, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid  FROM contact_details, contacts_connected_wallets where contact_details.uuid=(SELECT user_connected_Wallets.uuid FROM user_connected_Wallets WHERE user_connected_Wallets.wallet_address='{wallet_addr}' AND user_connected_Wallets.networkid={network_id}) AND contacts_connected_wallets.uuid=contact_details.uuid AND contacts_connected_wallets.contactid=contact_details.contactid;""")
        # select contact_details.room, contact_details.contactid, contacts_connected_wallets.wallet_address from contact_details, contacts_connected_wallets where contact_details.uuid='863dc52a-c39c-11ec-8b20-82304926de9b' AND contacts_connected_wallets.uuid=contact_details.uuid AND contact_details.contactid=contacts_connected_wallets.contactid;
        
        cursor.execute(f"""SELECT group_relation.room, contact_details.name, contact_details.primary_wallet_address, contacts_connected_wallets.wallet_address, contacts_connected_wallets.networkid 
        FROM group_relation, contact_details, contacts_connected_wallets 
        where group_relation.room_type='dm' 
        AND group_relation.uuid='{uuid}'
        AND contact_details.uuid=group_relation.uuid 
        AND contacts_connected_wallets.uuid=group_relation.uuid 
        AND CAST(group_relation.wallet_address AS INTEGER)=contacts_connected_wallets.contactid 
        AND contact_details.contactid=contacts_connected_wallets.contactid;""")

        rows = cursor.fetchall()
        # print(rows, '\n\n')

        # # Get DM room Names
        # dm_rooms=[]
        # for i in range(len(rows)):
        #     dm_rooms+=[rows[i][0]]
        # dm_rooms=tuple(set(dm_rooms))

        dm_rooms={'dm':{}}
        
        for i in range(len(rows)):
            if rows[i][0] not in dm_rooms['dm']:
                dm_rooms['dm'].update({
                    rows[i][0]:{
                        rows[i][1]:{
                            'primary_address':rows[i][2],
                            'wallet_address':[(rows[i][3], rows[i][4])]
                            }
                        }
                    }
                )

            else:
                dm_rooms['dm'][rows[i][0]][rows[i][1]]['wallet_address']+=[(rows[i][3], rows[i][4])]
        print(dm_rooms, '\n\n')


        # # 1<--->1
        # cursor.execute(f"""SELECT group_relation.room 
        # FROM group_relation
        # WHERE group_relation.room_type='dm' 
        # AND group_relation.uuid='{uuid}';""")

        # rows = cursor.fetchall()

        # total_group_rooms_query = str(rows)[1:-1].replace(')','').replace(',','').replace('(', 'OR group_relation.room=')[3:]
        # print(total_group_rooms_query, '\n\n')


        # cursor.execute(f"""SELECT group_relation.room, group_relation.name, group_relation.wallet_address, user_connected_wallets.networkid 
        # FROM group_relation, user_connected_wallets
        # WHERE ({total_group_rooms_query})
        # AND user_connected_wallets.wallet_address=group_relation.wallet_address;""")

        # rows = cursor.fetchall()

        # Group rooms one<--->many

        cursor.execute(f"""SELECT group_relation.room 
        FROM group_relation
        WHERE group_relation.room_type='group' 
        AND group_relation.uuid='{uuid}';""")

        rows = cursor.fetchall()

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
        print(group_rooms, '\n\n')

        
    # Fetch Conversation Data

    # cursor.execute(f"""SELECT * 
    # FROM communication_data
    # WHERE {total_group_rooms_query};""")

    # rows = cursor.fetchall()

    # print(rows, '\n\n')

    # For 1<--->1 conversation

    cursor.execute(f"""SELECT group_relation.room 
    FROM group_relation
    WHERE group_relation.room_type='dm' 
    AND group_relation.uuid='{uuid}';""")

    rows = cursor.fetchall()

    total_group_rooms_query = str(rows)[1:-1].replace(')','').replace(',','').replace('(', 'OR communication_data.room=')[3:]
    # print(total_group_rooms_query, '\n\n')
    
    cursor.execute(f"""SELECT communication_data.room, communication_data.sender, communication_data.timestamp, communication_data.msgdata, communication_data.room_type 
    FROM communication_data
    WHERE {total_group_rooms_query};""")

    rows = cursor.fetchall()

    print(rows, '\n\n')


    comm_data = {'communication_data':{}}
    for i in range(len(rows)):

        if rows[i][4]=='dm':
            if rows[i][1]==uuid:
                sender='you'
            else:
                sender='contact'
        else:
            if rows[i][1] in usr_basic_details['basic_data']['wallet_address']:
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
                    comm_data['communication_data']['dm'][rows[i][0]].update({
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

    print(comm_data, '\n\n')


    # For 1<--->many conversation
    
    cursor.execute(f"""SELECT group_relation.room 
    FROM group_relation
    WHERE group_relation.room_type='group' 
    AND group_relation.uuid='{uuid}';""")

    rows = cursor.fetchall()

    total_group_rooms_query = str(rows)[1:-1].replace(')','').replace(',','').replace('(', 'OR communication_data.room=')[3:]
    # print(total_group_rooms_query, '\n\n')
    
    cursor.execute(f"""SELECT communication_data.room, communication_data.sender, communication_data.timestamp, communication_data.msgdata 
    FROM communication_data
    WHERE {total_group_rooms_query};""")

    rows = cursor.fetchall()

    # print(rows, '\n\n')

    
    comm_data = {'communication_data':{'group':{}}}
    for i in range(len(rows)):
        
        if rows[i][1] in usr_basic_details['basic_data']['wallet_address']:
            sender='you'
        else:
            sender=rows[i][1]


        if rows[i][0] not in comm_data['communication_data']['group']:

            comm_data['communication_data']['group'].update({
                rows[i][0]:{
                    sender:{
                        rows[i][2]:{
                            'data': rows[i][3]
                        }
                    }
                }
            })
        
        else:

            if sender not in comm_data['communication_data']['group'][rows[i][0]]:
                comm_data['communication_data']['group'][rows[i][0]].update({
                    sender:{
                        rows[i][2]:{
                            'data': rows[i][3]
                        }
                    }
                })

            else:

                comm_data['communication_data']['group'][rows[i][0]][sender].update({
                    rows[i][2]:{
                        'data': rows[i][3]
                    }
                })

    print(comm_data, '\n\n')


    conn.commit() # <--- makes sure the change is shown in the database
    
    cursor.close()
    conn.close()
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


