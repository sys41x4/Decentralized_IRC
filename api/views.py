from ast import In
from ctypes import addressof
from logging import exception
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest, HttpResponseServerError, request
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from api.models import api
from user.models import user

import time
import uuid
import os, random
import binascii
import subprocess
import json, yaml
from web3 import Web3
import requests
from jwt import encode as jwt_encode
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
from . import utils
from .utils import is_logged_in # is_logged_in = decorator to check if user is logged in. Redirects to login page if not.
# Custom decorator to check authentication: https://stackoverflow.com/questions/5469159/how-to-write-a-custom-decorator-in-django

network_ID_data={}
msg_status = {0:'FAILED', 1:'SUCCESS'}
color = {0:'#e74c3c', 1:'#2ecc71'}


#Custom decorator to check authentication: https://stackoverflow.com/questions/5469159/how-to-write-a-custom-decorator-in-django

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

@is_logged_in
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

@is_logged_in
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

@csrf_protect
def access_chk(request):
    return JsonResponse({'Response Code':200})

@is_logged_in
@csrf_protect
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
                
        
        
# To delete
@csrf_protect
#@csrf_exempt
def set_wallet_session(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        wallet_address = data['wallet_address']

    return JsonResponse({'Response Code':200})

# Fetch JWTs for chat room authentication.
# Need to first verify if the user has access to the chat room whose token is request. Verification needs to be done using the database
# If no access, reject the request.
# JWT's payload will be of format {"rooms":[<list of all the rooms, checked using database>]}
#Room name payload format : UUID

@is_logged_in
@csrf_exempt
def fetch_chat_token(request):
    if request.method == 'POST': # and request.headers['wallet-address'] in access_to_rooms['room']
        encoded_data = utils.generate_auth_jwt(['test','test2'],'chat')
        token = {"access_token":encoded_data}
        return JsonResponse(token)



# Fetch JWTs for chat room authentication.
# Need to first verify if the user has access to the chat room whose token is request. Verification needs to be done using the database
# If no access, reject the request.
# JWT's payload will be of format {"rooms":[<list of all the rooms, checked using database>]}
#Room name payload format : UUID

@is_logged_in
@csrf_exempt
def fetch_chat_token(request):
    if request.method == 'POST': # and request.headers['wallet-address'] in access_to_rooms['room']
        encoded_data = utils.generate_auth_jwt(['test','test2'],'chat')
        token = {"access_token":encoded_data}
        return JsonResponse(token)

## Web3 Authnetication view

## Generate nonce
def generate_nonce(request):
    try:
        nonce = (str(uuid.uuid5(uuid.NAMESPACE_DNS, str(os.urandom(128))))+'-'+str(uuid.uuid1())).split('-')
        random.shuffle(nonce)
        nonce = '-'.join(nonce)
        # nonce = 'str(uuid.uuid4())'
        response = HttpResponse(json.dumps({"nonce":nonce}), content_type='application/json')
        response.set_cookie("nonce",value=nonce,httponly=True)
        return response
    except:
        return JsonResponse({"error":"something went wrong"})

# Authenticate
#<change to csrf_protect>
@csrf_protect
def web3_authentication(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        #try:
        data = json.loads(request.body)
        nonce = request.COOKIES['nonce']   #one time unique nonce
        #nonce_hex = HexBytes(nonce)
        signature = data['signature']   #signature
        signatue_hex = HexBytes(signature)
        print("signature hex",signatue_hex)
        w3 = Web3(Web3.HTTPProvider(""))
        message=encode_defunct(text=nonce) #encode msg
        print("message",message)
        user_address = data['wallet_address'].upper()
        verified_address = w3.eth.account.recover_message(message,signature=signatue_hex).upper()
        print("message verified",verified_address) #get account who generated the signature for this message
        if verified_address == user_address: #check if address matches with user's address
                # Perform DB operations here/ create account if the user is new, if not new but already exists, then authenticate 
            jwt = utils.generate_auth_jwt({'UID':'UID_FROM_DATABASE','Wallet_address':user_address},'auth')
            token_res = {"id_token":jwt,"redirect_uri":"/user/betamsg"}
            res = HttpResponse(json.dumps(token_res), content_type="application/json")
            res.set_cookie("id_token",value=jwt,httponly=True,secure=False) # id token = jwt !!CHANGE COOKIE FLAGS!! 
            res.delete_cookie("nonce") #Delete Nonce if auth successfull
            return res
        else:
            return JsonResponse({"error":"unable to authenticate at this time"})
    else:
        return HttpResponseBadRequest(JsonResponse({"error":"Bad Request"}))

#change to csrf_protect
@is_logged_in
@csrf_exempt
def logout(request):
   # res = JsonResponse({"redirect_uri":"/"})
   # Change to XHR, after implemnting logout button in common a js file
    res = HttpResponseRedirect('/')
    for i in request.COOKIES:
        res.delete_cookie(i)
    return res

gen_chain_list()
