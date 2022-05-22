from django.urls import path
from . import views

# urlpatterns = [
#     path("access_chk", views.access_chk, name="access_chk"),
#     path("chk_addr_validity", views.chk_addr_validity, name="chk_addr_validity"),
#     path("set_wallet", views.set_wallet_session, name="set_wallet_session"),
#     path("send_msg", views.send_msg, name="send_msg"),
#     path("fetch_messages", views.fetch_messages, name="fetch_messages"),
#     path("fetch_startup_data", views.fetch_startup_data, name="fetch_startup_data"),
#     path("fetch_contacts", views.fetch_contacts, name="fetch_contacts"),
#     path("fetch_uuid", views.fetch_uuid, name="fetch_uuid"),
#     path("fetch_indv_contact_details", views.fetch_indv_contact_details, name="fetch_indv_contact_details"),
#     path("chat_ids",views.chat_ids,name="fetch_chat_ids"),

#     path('fetch_chat_token',views.fetch_chat_token,name="fetch_chat_tokens"),
#     path('web3login',views.web3_authentication,name="web3_authentication"),
#     path('generate_nonce',views.generate_nonce,name="generate_nonce"),
#     path('logout',views.logout,name="logout handler")
# ]

urlpatterns = [
    path("access_chk", views.access_chk, name="access_chk"),
    path("chk_addr_validity", views.chk_addr_validity, name="chk_addr_validity"),
    path("set_wallet", views.set_wallet_session, name="set_wallet_session"),
    path("send_msg", views.send_msg, name="send_msg"),

    path('fetch_chat_token',views.fetch_chat_token,name="fetch_chat_tokens"),
    path('web3login',views.web3_authentication,name="web3_authentication"),
    path('generate_nonce',views.generate_nonce,name="generate_nonce"),
    path('logout',views.logout,name="logout handler")
]