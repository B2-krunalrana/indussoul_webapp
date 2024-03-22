# vcard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vcard_home, name='vcard_home'),
]
