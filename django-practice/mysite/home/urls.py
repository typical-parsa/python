from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/<username>', views.usershow),
    path('messages', views.message_show)
]