from django.urls import path
from . import views

urlpatterns = [
    path("access_chk", views.access_chk, name="access_chk"),
    path("send_msg", views.send_msg, name="send_msg"),
    path("set_wallet", views.set_wallet_session, name="set_wallet_session"),
]