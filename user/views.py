from django.shortcuts import render
from user.models import user

def homepage(request):
    return render(request, 'homepage.html')

def beta_message(request):
    # receiver = request.GET['r']
    # return render(request, 'beta_msg.html',{'recv':receiver})
    return render(request, 'beta_msg.html')

def user_dashboard(request):
    # Message = user.objects.all()
    # context = {
    #     'message': Message
    # }
    return render(request, 'dashboard.html')

def message_page(request):
    Message = user.objects.all()
    context = {
        'message': Message
    }
    return render(request, 'message.html', context)

def metamask_message_page(request):
    Message = user.objects.all()
    context = {
        'message': Message
    }
    return render(request, 'metamask_message.html', context)

def user_account(request):
    # Message = message.objects.get(pk=pk)
    Message = user.objects.all()
    context = {
        'message': Message
    }
    return render(request, 'account.html', context)

# Test for solana
def solana_test(request):
    Message = user.objects.all()
    context = {
        'message': Message
    }
    return render(request, 'solana.html', context)