from django.shortcuts import render
from user.models import user

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

def user_account(request):
    # Message = message.objects.get(pk=pk)
    Message = user.objects.all()
    context = {
        'message': Message
    }
    return render(request, 'account.html', context)