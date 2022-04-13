from django.urls import path
from . import views

urlpatterns = [
    path("message", views.message_page, name="message_page"),
    path("account", views.user_account, name="user_account"),
]