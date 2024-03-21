# from django.contrib import admin
from django.urls import path,include

from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(("accounts/"),include("django.contrib.auth.urls")),
    path(("singup/"),authView,name="authView"),
    path((""),include("django.contrib.auth.urls")),

]
