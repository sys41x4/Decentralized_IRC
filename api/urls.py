from django.urls import path
from . import views

urlpatterns = [
    path("access_chk", views.access_chk, name="access_chk"),
    path("chk_addr_validity", views.chk_addr_validity, name="chk_addr_validity"),
    path("set_wallet", views.set_wallet_session, name="set_wallet_session"),
    path("send_msg", views.send_msg, name="send_msg"),
    path("fetch_messages", views.fetch_messages, name="fetch_messages"),
]