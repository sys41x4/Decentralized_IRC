from ast import In
from logging import exception
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from api.models import api
from user.models import user

import time
import binascii
import subprocess
import json, yaml
from web3 import Web3
import requests

# # Load JSON data from chain_IDs.json file
# json_chain_ID_file_path = 'chain_IDs.json'
# chain_ID_data = json.load(open(json_chain_ID_file_path, encoding='utf-8'))

network_ID_data={}
msg_status = {0:'FAILED', 1:'SUCCESS'}
color = {0:'#e74c3c', 1:'#2ecc71'}

def gen_chain_list():
    # Generate Chain_ID data directly from https://chainlist.org/
    print("Gathering Data from https://chainlist.org/")
    global network_ID_data
    chainlist_response = requests.get('https://chainlist.org/')
    chain_lists = json.loads(chainlist_response.text.split("id=\"__NEXT_DATA__\" type=\"application/json\">")[1].split("</script></body></html>")[0])['props']['pageProps']['sortedChains']

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
            output = f"You: {sndr_address} & Receiver: {rcvr_address} validity is checked with\nRPC: {rpc}\n\nChain Detail: {yaml.dump(network_ID_data[networkId])}"
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

# def verify_UID(chainId):
#     rpc = chain_ID_data[chainId][rpc][0]

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
#@csrf_exempt
def set_wallet_session(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        wallet_address = data['wallet_address']

    return JsonResponse({'Response Code':200})

# Fetch messages from etherium explorer and return JSON.
@csrf_exempt
def getMessages(request):
    try:
        if request.method == 'POST' and request.content_type == 'application/json':
            data = json.loads(request.body)
            wallet_address = data['wallet_address']
            transactions = requests.get(f'https://api-kovan.etherscan.io/api?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=asc&apikey=V9EAM35F8F1RGRD3EPJAQQ4N97K9M37GMV',headers={"User-Agent":"IRC-DEV"})
            transactions_json = transactions.json()
            transactions_json_len = len(transactions_json['result'])
            transactions_dict ={"sent":{},"received":{}}
            for i in range(0,transactions_json_len):
                sender_address = transactions_json['result'][i]['from']
                receiver_address = transactions_json['result'][i]['to']
                message_hex = transactions_json['result'][i]['input']
                if sender_address == wallet_address:
                    if receiver_address not in transactions_dict['sent']:
                        transactions_dict['sent'][receiver_address] = []
                        transactions_dict['sent'][receiver_address].append(message_hex)
                    else:
                        transactions_dict['sent'][receiver_address].append(message_hex)
                elif receiver_address == wallet_address:
                    if sender_address not in transactions_dict['received']:
                        transactions_dict['received'][sender_address] = []
                        transactions_dict['received'][sender_address].append(message_hex)
                    else:
                        transactions_dict['sent'][sender_address].append(message_hex)
            response_json = {"result":transactions_dict}
            return JsonResponse(response_json)
        else:
            return HttpResponseBadRequest()
    except:
        return HttpResponseServerError("Something Went Wrong")
    return JsonResponse({'Response Code':200})
  
gen_chain_list()
