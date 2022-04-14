from django.shortcuts import render
# from Decentralized_IRC.models import Decentralized_IRC

def homepage(request):
    return render(request, 'homepage.html')