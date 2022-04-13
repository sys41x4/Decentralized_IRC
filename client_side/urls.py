from django.urls import path
from client_side import views

urlpatterns = [
    path('hello', views.client_side, name='client_side'),
]