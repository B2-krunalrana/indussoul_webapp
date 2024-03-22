from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect



@login_required
def home(request):
    
    return render(request,"index.html",{'user': request.user})

def authView(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form=UserCreationForm()
    return render(request,"registration/signup.html",{"form":form})

def logout_view(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return redirect('login')  # Redirect to the login page after logout
    
def user_account(request):
    return render(request,"account.html",{'user': request.user})

def user_vcard_template(request):
    return render(request,"userVcardTemplate.html",{'user': request.user})

def user_setting(request):
    return render(request,"setting.html",{'user': request.user})



