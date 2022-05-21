from django.shortcuts import redirect, render
from user.models import user
from api.utils import is_logged_in

def homepage(request):
    return render(request, 'homepage.html')

@is_logged_in
def beta_message(request):
    # receiver = request.GET['r']
    # return render(request, 'beta_msg.html',{'recv':receiver})
    if 'id_token' in request.COOKIES:
        return render(request, 'beta_msg.html')
    else:
        return redirect('/user/login')

@is_logged_in
def user_dashboard(request):
    # Message = user.objects.all()
    # context = {
    #     'message': Message
    # }
    if 'id_token' in request.COOKIES:
        return render(request, 'dashboard.html')
    else:
        return redirect('/user/login')

@is_logged_in
def message_page(request):
    Message = user.objects.all()
    context = {
        'message': Message
    }
    if 'id_token' in request.COOKIES:
        return render(request, 'message.html')
    else:
        return redirect('/user/login')

@is_logged_in
def metamask_message_page(request):
    Message = user.objects.all()
    context = {
        'message': Message
    }
    if 'id_token' in request.COOKIES:
        return render(request, 'metamask_message.html')
    else:
        return redirect('/user/login')

@is_logged_in
def user_account(request):
    # Message = message.objects.get(pk=pk)
    Message = user.objects.all()
    context = {
        'message': Message
    }
    if 'id_token' in request.COOKIES:
        return render(request, 'account.html')
    else:
        return redirect('/user/login')

# Test for solana
def solana_test(request):
    Message = user.objects.all()
    context = {
        'message': Message
    }
    return render(request, 'solana.html', context)

def login(request):
    return render(request,'login.html')
