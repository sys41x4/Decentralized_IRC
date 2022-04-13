from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from api.models import api
from user.models import user

# @csrf_protect
@csrf_exempt
def send_msg(request):
    Message = api.objects.all()
    if request.method == "POST":
       return HttpResponse("OK hey")
    #     data = request.get_json()
    #     sender = data['sender']
    #     receiver =  data['receiver']
    #     message = binascii.hexlify(data['message'].encode()).decode()
    #     output = sender + ' -> ' + receiver + ' | ' + message
    #     print({'sender':sender, 'receiver':receiver, 'message':message})
    #     if sender and receiver and message:

    #         Txn_Hash = 'Txn-Hash' # test Txn Hash

    #         block_data = {
    #         "From" : sender,
    #         "To" : receiver,
    #         "Block" : '<Previous Block Number>+1',
    #         "Timestamp" : time.time(),
    #         "Parent-Hash" : "Previous Transaction Hash",
    #         "Txn-Hash" : 'New_Hash(<Previous Txn-Hash>+<New File Hash>)',
    #         "Mined-by" : 'Miner-Hash',
    #         "Charge" : 'Price-For-messaging [Free/Paid]',
    #         "Size" : "Data-Size",
    #         "Nonce" : "Nonce-Value",
    #         "Comment" : message,
    #         "Status" : "<0/1>"
    #         }
    context = {
        'message': Message
    }
    
    #return render(request, 'message_index.html', context)
    return HttpResponse("OK")
# @csrf_protect
@csrf_exempt
def set_wallet_session(request):
    # Message = api.objects.get(pk=pk)
    Message = api.objects.all()
    context = {
        'message': Message
    }
    return HttpResponse("OK")