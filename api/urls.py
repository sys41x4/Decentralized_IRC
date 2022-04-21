from django.urls import path
from . import views

urlpatterns = [
    path("send_msg", views.send_msg, name="send_msg"),
    path("set_wallet", views.set_wallet_session, name="set_wallet_session"),
    path("getMessages",views.getMessages,name='get_contacts')
]