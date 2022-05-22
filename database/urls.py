from django.urls import path
from . import views

urlpatterns = [
    path("startup_data", views.startup_data, name="startup_data"),
]