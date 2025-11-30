from django.urls import path
from . import views

urlpatterns = [
    path("adduser", views.user_signup_page)
]