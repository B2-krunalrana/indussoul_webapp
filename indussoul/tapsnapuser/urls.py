# from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("user_account/", user_account, name="user_account"),
    path("user_setting/", user_setting, name="user_setting"),
    path("user_vcard_template/", user_vcard_template, name="user_vcard_template"),
]

# user login-logout routs 
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),
    path("logout/", logout_view, name="logout"),
]
