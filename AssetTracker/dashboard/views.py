from urllib import request

from django.shortcuts import render, redirect
# from .models import Employee
from django.contrib import messages
#from .models import MainDashBoard, Asset_Allocation
from django.views.decorators.csrf import requires_csrf_token
from .forms import *



def AssetFormView(request):
    # Retrieve the required data from the database
    asset_form = AssetForm.objects.get(name='Assetform.html')

    # Pass the data to the template
    return render(request, '../templates/Assetform.html', {'asset_form': asset_form})
def home(request):
    Types = MainDashBoard.objects.all()

    context = {
        'types': Types,
    }

    return render(request, '../templates/index.html', context)


def table(request):
    return render(request, '../templates/tables.html')



@requires_csrf_token
def add_details(request):
    if request.method == 'POST':  # Validate the Form post == post: True
        asset_allocation = Asset_Allocation()
        asset_allocation.Employee_name = request.POST['Employee_name']
        asset_allocation.Employee_id = request.POST['Employee_id']
        asset_allocation.Group = request.POST['Group']
        #asset_allocation.Sub_Group = request.POST['Sub_Group']
        asset_allocation.Contact_number = request.POST['Contact_number']
        #asset_allocation.Working_For_Client = request.POST['Working_For_Client']
        asset_allocation.Client_Email_id = request.POST['Client_Email_id']
        asset_allocation.Laptop = request.POST['Client_Laptop']
        asset_allocation.Client_Mouse = request.POST['Client_Mouse']
        asset_allocation.Client_Headphones = request.POST['Client_Headphones']
        asset_allocation.Client_Computer = request.POST['Client_Computer']
        asset_allocation.Client_Remarks = request.POST['Client_Remarks']
        #asset_allocation.Employee_Status = request.POST['Employee_Status']
        asset_allocation.BI_Email_id = request.POST['BI_Email_id']
        asset_allocation.BI_Laptop = request.POST['BI_Laptop']
        asset_allocation.BI_Mouse = request.POST['BI_Mouse']
        asset_allocation.BI_Headphones = request.POST['BI_Headphones']
        asset_allocation.BI_Computer = request.POST['BI_Computer']
        asset_allocation.BI_Remarks = request.POST['BI_Remarks']
        asset_allocation.save()
        messages.error(request, 'Failed to add product. Please try again.')
        return redirect('../templates/Assetform.html')
    else:
        messages.error(request, 'Failed to add product. Please try again.')
    return render(request, '../templates/Assetform.html')


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponseRedirect
# #from django.shortcuts import render_to_response


# def render_to_response(param, param1):
#     pass


class Asset_Allocation_Form:
    print("rendering ")
    pass


def register(request):
    if request.method == 'POST':
        form = Asset_Allocation_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../templates/Assetform")
    else:
        form = Asset_Allocation_Form()

    return render(request, "../templates/Assetform.html", {
        'form': form,
    })


def NewJoinerreport(request):
    Client_Assets = Asset_Allocation_Form.objects.filter(
        Working_For_Client=True)  # I am feteching all the row from the product table

    context = {
        'client_assets': Client_Assets
    }
    return render(request, '../templates/client.html', context)
def Asseetform(requst):
    return render(request, '../templates/Assetform.html')
def submit_form(request):
    if request.method == 'POST':
        # Perform the necessary actions here
        return redirect('success')  # Redirect to a success page
    else:
        return render(request, 'Assetform.html')

def success(request):
    return render(request, 'C:/Users/vmuthyala/PycharmProjects/AssetTracker/AssetTracker/dashboard/templates/success.html')
def dashboard(request):
    data = MainDashBoard.objects.all()
    return render(request, 'dashboard.html', {'data': data})
