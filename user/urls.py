from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_dashboard, name="user_dashboard"),
    path("message", views.message_page, name="message_page"),
    path("metamask_message", views.metamask_message_page, name="metamask_message_page"),
    path("account", views.user_account, name="user_account"),
    path("homepage", views.homepage, name="homepage"),
    path("betamsg", views.beta_message, name="beta_message"),
    path("solana",views.solana_test,name="solana_test" )

]