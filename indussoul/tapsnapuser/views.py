from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def authView(request):
    form=UserCreationForm()
    return render(request,"/singnup.html",{"form":form})