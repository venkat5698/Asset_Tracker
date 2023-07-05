from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def loginpage(request):
    return render(request,'../templates/login.html')
def forgotpasswordpage(request):
    return render(request,'../templates/password.html')
def registerpage(request):
    print("new")
    return render(request,'../templates/register.html')