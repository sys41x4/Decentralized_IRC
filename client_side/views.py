from django.shortcuts import render

# Create your views here.
def client_side(request):
    return render(request, 'hello_world.html', {})