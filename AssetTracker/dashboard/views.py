from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def dashboardpage(request):
    return render(request, '../templates/index.html')
def layoutpage(request):
    return render(request, '../templates/layout-static.html')
