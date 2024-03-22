from django.shortcuts import render

def vcard_home(request):
    # return render(request, '/vcard/template/vcard_home.html')
    return render(request, 'vcard_home.html')