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
import json

# @csrf_protect
@csrf_exempt
def send_msg(request):
    # Message = api.objects.all()
    if request.method == "POST":
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

            block_data = {
            "From" : sender,
            "To" : receiver,
            "Block" : '<Previous Block Number>+1',
            "Timestamp" : time.time(),
            "Parent-Hash" : "Previous Transaction Hash",
            "Txn-Hash" : 'New_Hash(<Previous Txn-Hash>+<New File Hash>)',
            "Mined-by" : 'Miner-Hash',
            "Charge" : 'Price-For-messaging [Free/Paid]',
            "Size" : "Data-Size",
            "Nonce" : "Nonce-Value",
            "Comment" : message,
            "Status" : "<0/1>"
            }
        # Commented the upload data to IPFS functions
        # After testing the paid transactions, the Free Transactions can be implemented

            with open(Txn_Hash, 'w') as test_file:
                test_file.write(json.dumps(block_data))

            # os.popen('node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc test_data.json').read()
            print('uploading file to IPFS')
            ## Upload Conversation File ##
            # print(os.getcwd())
            # print("getting if there is any file", os.path.exists("put-files.js"))
            Upload_file = subprocess.Popen(["node", "put-files.js", "--token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc", 'txn_hashes/'+Txn_Hash], stdout=subprocess.PIPE, shell=True)
            print('file uploaded')
            (CID_byte, err) = Upload_file.communicate()
            CID = CID_byte.decode().replace('\n','').split(": ")[1]
            # Get the uploaded File -> https://<CID>+.ipfs.dweb.link/<FileName>
            print("CID Output => ", CID)

            # Command Used to get the Txn-Hash Content
            print(f'curl https://{CID}.ipfs.dweb.link/{Txn_Hash}')
            # File to get https://<CID>+.ipfs.dweb.link/<Txn-Hash>

            
            return JsonResponse({'output': output})
        return JsonResponse({'error' : 'Missing data!'})
    # context = {
    #     'message': Message
    # }
    
    #return render(request, 'message_index.html', context)
    return HttpResponse("OK")
# @csrf_protect
@csrf_exempt
def set_wallet_session(request):
    # Message = api.objects.get(pk=pk)
    # Message = api.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        wallet_address = data['wallet_address']
    #session['wallet_address'] = wallet_address
    # context = {
    #     'message': Message
    # }
    return HttpResponse("OK")