from ast import In
from ctypes import addressof
from logging import exception
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from api.models import api
from user.models import user

import time
import uuid
import binascii
import subprocess
import json, yaml
from web3 import Web3
import requests



network_ID_data={}
msg_status = {0:'FAILED', 1:'SUCCESS'}
color = {0:'#e74c3c', 1:'#2ecc71'}

def gen_chain_list():
    global network_ID_data
    # # Generate Chain_ID data directly from https://chainlist.org/
    # print("Gathering Data from https://chainlist.org/")
    # chainlist_response = requests.get('https://chainlist.org/')
    # chain_lists = json.loads(chainlist_response.text.split("id=\"__NEXT_DATA__\" type=\"application/json\">")[1].split("</script></body></html>")[0])['props']['pageProps']['sortedChains']

    # # Load JSON data from chain_IDs.json file
    print("Gathering Data from https://chainlist.org/ generated json File")
    json_chain_ID_file_path = 'chain_ID_list.json'
    chain_lists = json.load(open(json_chain_ID_file_path, encoding='utf-8'))['props']['pageProps']['sortedChains']

    for basic_chain_detail_index in range(len(chain_lists)):
        try:
            network = chain_lists[basic_chain_detail_index]['network']
            explorers = chain_lists[basic_chain_detail_index]['explorers']
            rpc = chain_lists[basic_chain_detail_index]['rpc']
        except KeyError:
            network = ''
            explorers = ''
            rpc=[]

        network_ID_data.update({
            chain_lists[basic_chain_detail_index]["networkId"]:{
                "name":chain_lists[basic_chain_detail_index]['name'],
                "chain":chain_lists[basic_chain_detail_index]['chain'],
                "rpc":rpc,
                "network":network,
                "nativeCurrency":chain_lists[basic_chain_detail_index]['nativeCurrency'],
                "explorers":explorers,
                "shortName":chain_lists[basic_chain_detail_index]['shortName'],
                "chainId":chain_lists[basic_chain_detail_index]['chainId'],
                "networkId":chain_lists[basic_chain_detail_index]['networkId']
                }
            })

# # # Get RPCs List
# rpcinfo_response = requests.get('https://rpc.info/static/js/main.chunk.js')
# rpc_lists = json.loads(rpcinfo_response.text.split('const RPCS = [// avax')[1].split('\n\nvar _c;')[0])

@csrf_protect
def chk_addr_validity(request):
    # Get RPC Network Details from https://rpc.info/
    # Using Kovan TestNet for testing
    # RPC HTTP Link https://kovan.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161
    # Identify using Chain ID https://chainlist.org/
    # rpc_http_link_list = {
    #     "KOVAN":"https://kovan.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"
    #     }
    if request.method == "POST":
        
        try:
            global network_ID_data
            # print(network_ID_data[42])
            data = json.loads(request.body)
            # print(request.POST)
            networkId = int(data['networkID'])
            sndr_address = data['sender_address']
            rcvr_address =  data['receiver_address']
            rpc = network_ID_data[networkId]['rpc'][0]
            w3 = Web3(Web3.HTTPProvider(rpc))
            chk_sndr_addr = w3.isAddress(sndr_address)
            chk_rcvr_addr = w3.isAddress(rcvr_address)
            output = f"You: {sndr_address} & Receiver: {rcvr_address} validity is checked with\nRPC: {rpc}\n\nChain Detail: \n{yaml.dump(network_ID_data[networkId])}"
            # print(chk_addr, output)
            if ((chk_sndr_addr == True) and (chk_rcvr_addr == True)):
                return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': f"You: {sndr_address}\nReceiver: {rcvr_address} is valid\n\n{output}"})
            elif ((chk_sndr_addr == True) or (chk_rcvr_addr == True)):
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': f"You: {sndr_address}\nReceiver: {rcvr_address} is invalid\n\n{output}"})

        except:
            output = "An ERROR occured"
            # print(output)
            return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})


# def fetch_CurrentUser_walletAddresses(uuid, wallet_addr):
uuid_linked_walletAddr={
    '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9':'863dc52a-c39c-11ec-8b20-82304926de9b',
    '0X283C3B6A4D84D457F1B6BB8FB947CFA432EFC293':'863dc52a-c39c-11ec-8b20-82304926de9b',
    '0XFFE39E1461D0361C3D72658EF39AE76288C82622':'a149137f-c39b-11ec-81f4-82304926de9b',
    '0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9':'a149137f-c39b-11ec-81f4-82304926de9b',
    '0X68237960F18F2B3A1555A39CD3427C52B98AD10B':'6905735c-c511-11ec-a9f3-82304926de9b',
    '0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B':'5fa6aee8-cf80-11ec-9735-82304926de9b',

}


basic_user_detail = {
    '863dc52a-c39c-11ec-8b20-82304926de9b': {
        'name':'Arijit Bhowmick',
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
        'primary_wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
        'connected_wallets':[
            {
                'wallet_address':'0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B',
                'networkId':42,
            }
        ]
    },

    'uNveRiF1eD_d4TA':{
        'name':'',
        'primary_wallet_address':'',
        'connected_wallets':[
            {
                'wallet_address':'',
                'networkId':'',
            }
        ]
    }
}

contact_details = {
    '863dc52a-c39c-11ec-8b20-82304926de9b': {
        'totalContacts':3,
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
        'totalContacts':1,
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
            }
        },
    },
        
    '6905735c-c511-11ec-a9f3-82304926de9b': {
        'totalContacts':3,
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
        'totalContacts':2,
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

    'UNv3RifiEd_DA74': {
        'totalContacts':0,
        'contactsList':{},

    },
}


communication_data = {

    '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9-0XFFE39E1461D0361C3D72658EF39AE76288C82622':{
        1650707120.936152: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':0, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'Hello Man Whats Up', 'networkId':42, 'timestamp':1650707120.936152},
        1650707282.4517663: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':1, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'What\'s going on ?', 'networkId':42, 'timestamp':1650707282.4517663},
        1650707328.6830337: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':2, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'I am just watching a movie...', 'networkId':42, 'timestamp':1650707328.6830337},
        1650707338.0125976: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':3, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'Hey Man Are You Still there ?', 'networkId':42, 'timestamp':1650707338.0125976},
        1650707348.8427203: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':4, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'Mannn.. Again you are offline ... -_- ', 'networkId':42, 'timestamp':1650707348.8427203},
        1650707156.6189778: {'sender':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'nonce':0, 'receiver':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'message':'I am good what\'s you doing ? ', 'networkId':42, 'timestamp':1650707156.6189778},
        1650707290.8573165: {'sender':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'nonce':1, 'receiver':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'message':'Nothing much, Just chilling with laptop', 'networkId':42, 'timestamp':1650707290.8573165},
    },
    
    
}

def fetch_uuid(request):
    if request.method == "POST":
        try:

            data = json.loads(request.body)
            
            try:
                uuid = uuid_linked_walletAddr[data['current_WalletAddress']]
                return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': 'Account Data Found', 'uuid':uuid})
            except:
                # return ('UUID Not Verified', basic_user_detail['uNveRiF1eD_d4TA'])
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'Verification Failed', 'uuid':'n0T v3RIfiEd'})

        except:
            output = "An ERROR occured\nAccount Verification Failed"
            # print(output)
            return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})


def fetch_startup_data(request):
    if request.method == "POST":
        try:
            # Parameters
            # # Fetcher:
            # ('self', 'current_WalletAddress')
            # 


            data = json.loads(request.body)
            # addressesOf = data['addressesOf']
            # uuid = data['uuid']
            wallet_addr = data['current_WalletAddress']

            try:
                uuid = uuid_linked_walletAddr[wallet_addr]
            except:
                # return ('UUID Not Verified', basic_user_detail['uNveRiF1eD_d4TA'])
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'UUID Not Verified', 'basic_UserData':basic_user_detail['uNveRiF1eD_d4TA']})

            

            # if addressesOf=='self':

            counter=0
            if (uuid in basic_user_detail):
                for i in basic_user_detail[uuid]['connected_wallets']:
                    if wallet_addr == i['wallet_address']:
                        counter+=1
    
                if (counter<1 or counter>1):return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'Wallet Address Not Verified', 'basic_UserData':basic_user_detail['uNveRiF1eD_d4TA']})
                    # return ('Wallet Address Not Verified', basic_user_detail['uNveRiF1eD_d4TA'])

                # return (uuid, basic_user_detail[uuid])
                return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': 'Successfully Fetched, Basic User Data', 'basic_UserData':[uuid, basic_user_detail[uuid]]})

            else:
                # return ('UUID Not Verified', basic_user_detail['uNveRiF1eD_d4TA'])
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'UUID Not Verified', 'basic_UserData':basic_user_detail['uNveRiF1eD_d4TA']})
                
            # elif addressesOf=='contact':
            #     contact_id = data['contact_id']
            #     active_rcvr_wltAddr = data['active_receiver_WalletAddress']
                
        except:
            output = "An ERROR occured\nStartup Data not fetched Successfully"
            # print(output)
            return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})


def fetch_contacts(request):
    if request.method == "POST":
        try:
            # Parameters
            # # Fetcher:
            # ('uuid', 'current_WalletAddress')
            # 
            data = json.loads(request.body)
            uuid = data['uuid']
            walt_addr= data['current_WalletAddress']
            # Assuming that we have implemented a function
            # where user can add multiple wallet address of his/her own
            # so there must be a identifier for that user whose wallet_addresses
            # will be collected as a list
            # 
            # Here comes the uid, where a random uid will be assigned to a user at first run
            # when he/she will trigger any request that lead to access to database
            # 
            # At that point the user will be assigned with a uid
            # after it is checked if the uid is allocated by other used or not
            # from the uid table data fetched from database
            # and the user's current wallet address will be added to the list of wallet_addresses
            # that the uid refer to.
            # 
            # Further details will be provided soon

            # # Using Test data for wallet_addresses list
            # # with predefined wallet_Address

            # Currently we are using UUID based on the host ID and current time
            # uid = uuid.uuid1()
            
            if uuid==uuid_linked_walletAddr[walt_addr]:
                # return contact_details[uuid]
                return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': 'Successfully Fetched Contact List', 'contact_list':contact_details[uuid]})

            else:
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'Verification Failed', 'contact_list':contact_details['UNv3RifiEd_DA74']})
            

            

        except:
                output = "An ERROR occured\nContacts are not fetched Successfully"
                # print(output)
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})


def fetch_indv_contact_details(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            uuid = data['uuid']
            walt_addr= data['current_WalletAddress']
            rcvr_pmry_addr = data['rcvr_pmry_addr']


    #         '5fa6aee8-cf80-11ec-9735-82304926de9b': {
    #     'totalContacts':2,
    #     'contactsList':{
    #         0:{
    #             'name': 'Arijit Bhowmick',
    #             'primary_wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
    #             'walletList':[
    #                 {
    #                     'wallet_address':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
    #                     'networkId':42,
    #                 }
    #             ]
    #         },

    #         1:{
    #             'name': 'Suraj Disoja',
    #             'primary_wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
    #             'walletList':[
    #                 {
    #                     'wallet_address':'0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
    #                     'networkId':42,
    #                 }

    #             ]
    #         }
    #     },

    # },

            if (uuid==uuid_linked_walletAddr[walt_addr]):

                for i in range(contact_details[uuid]['totalContacts']):
                    if rcvr_pmry_addr==contact_details[uuid]['contactsList'][i]['primary_wallet_address']:
                        return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': 'Contact Data Fetched Successfully', 'contact_detail':contact_details[uuid]['contactsList'][i]})
            
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'Verification Failed', 'contact_detail':contact_details['UNv3RifiEd_DA74']})

    
            else:
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': 'Verification Failed', 'contact_detail':contact_details['UNv3RifiEd_DA74']})



        except:
            output = "An ERROR occured\nContact detail not fetched Successfully"
            # print(output)
            return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})


def fetch_paid_txn(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            txn_hash = data['txn_hash']
            networkId = int(data['networkID'])
            rpc = network_ID_data[networkId]['rpc'][0]
            w3 = Web3(Web3.HTTPProvider(rpc))
            txn_data = w3.eth.get_transaction(txn_hash)
            data = bytes.fromhex(txn_data['input'][2:]).decode('utf-8')

        except:
            output = "An ERROR occured"
            # print(output)
            return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})

def fetch_messages(request):
    if request.method == "POST":
        try:
            # Considering that we have fetched correct data from database server
            # First the fetcher data will be fetched according to nonce value to a particular receiver
            # Then the receivers data similarly
            # About the conversation between
            # 0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9 & 0X8CCEF537C24864F566B29FA11ED0ADC113B7BAF9
            # Only the Upper two addresses are considered for now
            # for testing purpose.
            # Where both are sender and reveiver
            # last 10 messages will be fetched to reduce unnecessary workload in the application

            data = json.loads(request.body)
            fetcher = data['fetcher']
            receiver = data['receiver']

            # Test Communication Data

            # communicators = {'fetcher':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622'}
            # if (f"{fetcher}-{receiver}" in communication_data) and (f"{}-{receiver}"):
                # output = f"Messages Fetched Successfully\nTotal 0 Messages fetched between {fetcher} & {receiver}"

                # return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': output, 'message_data':[]})

            # communication_data = {

            #     '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9-0XFFE39E1461D0361C3D72658EF39AE76288C82622':{
            #         1650707120.936152: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':0, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'Hello Man Whats Up', 'networkId':42, 'timestamp':1650707120.936152},
            #         1650707282.4517663: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':1, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'What\'s going on ?', 'networkId':42, 'timestamp':1650707282.4517663},
            #         1650707328.6830337: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':2, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'I am just watching a movie...', 'networkId':42, 'timestamp':1650707328.6830337},
            #         1650707338.0125976: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':3, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'Hey Man Are You Still there ?', 'networkId':42, 'timestamp':1650707338.0125976},
            #         1650707348.8427203: {'sender':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'nonce':4, 'receiver':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'message':'Mannn.. Again you are offline ... -_- ', 'networkId':42, 'timestamp':1650707348.8427203},
            #     },
                
            #     '0XFFE39E1461D0361C3D72658EF39AE76288C82622-0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9':{
            #         1650707156.6189778: {'sender':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'nonce':0, 'receiver':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'message':'I am good what\'s you doing ? ', 'networkId':42, 'timestamp':1650707156.6189778},
            #         1650707290.8573165: {'sender':'0XFFE39E1461D0361C3D72658EF39AE76288C82622', 'nonce':1, 'receiver':'0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9', 'message':'Nothing much, Just chilling with laptop', 'networkId':42, 'timestamp':1650707290.8573165},
            #     },
                
                
            # }
            
            if (f"{fetcher}-{receiver}" in communication_data):
                key = f"{fetcher}-{receiver}"
            elif (f"{receiver}-{fetcher}" in communication_data):
                key = f"{receiver}-{fetcher}"
            else:
                key = 0

            if key == 0:return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': f"Messages Fetched Successfully\nTotal 0 Messages fetched between {fetcher} & {receiver}"})
            ordered_message_data = []
            total_msg_count = len(communication_data[key])
        

            for timestamp in sorted(communication_data[key]):
                ordered_message_data+=[communication_data[key][timestamp]]

            output = f"Messages Fetched Successfully\nTotal {total_msg_count} Messages fetched between {fetcher} & {receiver}"

            return JsonResponse({'msg_status': msg_status[1], 'chatroom_id': 'test','color': color[1], 'output': output, 'message_data':ordered_message_data})

        except:
                output = "An ERROR occured\nMessages are not fetched Successfully"
                # print(output)
                return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'output': output})
    return JsonResponse({'Response Code':200})
        

@csrf_protect
def access_chk(request):
    return JsonResponse({'Response Code':200})

@csrf_protect
#@csrf_exempt
def send_msg(request):

    # Message = api.objects.all()
    if request.method == "POST":
        try:
        #return HttpResponse("OK hey")
            data = json.loads(request.body)
            # print(request.POST)
            sender = data['sender']
            receiver =  data['receiver']
            message = binascii.hexlify(data['message'].encode()).decode()
            output = sender + ' -> ' + receiver + ' | ' + message
            print({'sender':sender, 'receiver':receiver, 'message':message})
            if sender and receiver and message:

                Txn_Hash = 'Txn-Hash' # test Txn Hash

            #     block_data = {
            #     "From" : sender,
            #     "To" : receiver,
            #     "Block" : '<Previous Block Number>+1',
            #     "Timestamp" : time.time(),
            #     "Parent-Hash" : "Previous Transaction Hash",
            #     "Txn-Hash" : 'New_Hash(<Previous Txn-Hash>+<New File Hash>)',
            #     "Mined-by" : 'Miner-Hash',
            #     "Charge" : 'Price-For-messaging [Free/Paid]',
            #     "Size" : "Data-Size",
            #     "Nonce" : "Nonce-Value",
            #     "Comment" : message,
            #     "Status" : "<0/1>"
            #     }
            # # Commented the upload data to IPFS functions
            # # After testing the paid transactions, the Free Transactions can be implemented

            #     with open('txn_hashes/'+Txn_Hash, 'w') as test_file:
            #         test_file.write(json.dumps(block_data))

            #     # os.popen('node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc test_data.json').read()
            #     print('uploading file to IPFS')
            #     ## Upload Conversation File ##
            #     # print(os.getcwd())
            #     # print("getting if there is any file", os.path.exists("put-files.js"))
            #     Upload_file = subprocess.Popen(["node", "put-files.js", "--token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc", 'txn_hashes/'+Txn_Hash], stdout=subprocess.PIPE, shell=True)
            #     print('file uploaded')
            #     (CID_byte, err) = Upload_file.communicate()
            #     CID = CID_byte.decode().replace('\n','').split(": ")[1]
            #     # Get the uploaded File -> https://<CID>+.ipfs.dweb.link/<FileName>
            #     print("CID Output => ", CID)

            #     # Command Used to get the Txn-Hash Content
            #     print(f'curl https://{CID}.ipfs.dweb.link/{Txn_Hash}')
            #     # File to get https://<CID>+.ipfs.dweb.link/<Txn-Hash>

            # # msg_status = 'SUCCESS'
            # # color = '#2ecc71'
            return JsonResponse({'msg_status': msg_status[1],  'color': color[1], 'output': output})
        except KeyError as err:
            return JsonResponse({'msg_status': msg_status[0], 'color': color[0], 'error' : f"Error : {err} value is not provided"})
        except BaseException as err:
            return JsonResponse({'msg_status': msg_status[0],  'color': color[0], 'error' : f"Error : {err=}"})

    return JsonResponse({'Response Code':200})

@csrf_protect
def chat_ids(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = data['user']
        print("vmro User", user)

        # res = {"chats":{
        #         "room2":[
        #             '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
        #             '0XFFE39E1461D0361C3D72658EF39AE76288C82622'
        #         ],
        #     },    
        # }

        res = {
            '06d00a2cd16b11ecb96682304926de9b':[
                '0XD17D369FFFCD92E713CF482E6ECEDA693BF7C8B9',
                '0XFFE39E1461D0361C3D72658EF39AE76288C82622'
            ],

            '0834fa43d16b11ec950282304926de9b':[
                '0X68237960F18F2B3A1555A39CD3427C52B98AD10B',
                '0XF7EB78ED74E17A775098F3F8ADDA69B13942F96B'
            ]
        }

        for i in res:
            if user in res[i]:
                return JsonResponse({'chats':{i:[res[i]]}})
        return JsonResponse(res)
                
        
        

@csrf_protect
#@csrf_exempt
def set_wallet_session(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        wallet_address = data['wallet_address']

    return JsonResponse({'Response Code':200})

# # Fetch messages from etherium explorer and return JSON.
# @csrf_exempt
# def getMessages(request):
#     try:
#         if request.method == 'POST' and request.content_type == 'application/json':
#             data = json.loads(request.body)
#             wallet_address = data['wallet_address']
#             transactions = requests.get(f'https://api-kovan.etherscan.io/api?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=asc&apikey=V9EAM35F8F1RGRD3EPJAQQ4N97K9M37GMV',headers={"User-Agent":"IRC-DEV"})
#             transactions_json = transactions.json()
#             transactions_json_len = len(transactions_json['result'])
#             transactions_dict ={"sent":{},"received":{}}
#             for i in range(0,transactions_json_len):
#                 sender_address = transactions_json['result'][i]['from']
#                 receiver_address = transactions_json['result'][i]['to']
#                 message_hex = transactions_json['result'][i]['input']
#                 if sender_address == wallet_address:
#                     if receiver_address not in transactions_dict['sent']:
#                         transactions_dict['sent'][receiver_address] = []
#                         transactions_dict['sent'][receiver_address].append(message_hex)
#                     else:
#                         transactions_dict['sent'][receiver_address].append(message_hex)
#                 elif receiver_address == wallet_address:
#                     if sender_address not in transactions_dict['received']:
#                         transactions_dict['received'][sender_address] = []
#                         transactions_dict['received'][sender_address].append(message_hex)
#                     else:
#                         transactions_dict['sent'][sender_address].append(message_hex)
#             response_json = {"result":transactions_dict}
#             return JsonResponse(response_json)
#         else:
#             return HttpResponseBadRequest()
#     except:
#         return HttpResponseServerError("Something Went Wrong")
#     return JsonResponse({'Response Code':200})
  
gen_chain_list()
