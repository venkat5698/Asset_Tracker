from django import forms
from .models import Employee, Asset_Allocation, MainDashBoard

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class Asset_Allocation_Forms(forms.ModelForm):
    employee_status = forms.ModelChoiceField(queryset=MainDashBoard.objects.all().values_list('Catagory_name','s_no'),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Asset_Allocation
        fields = ["Employee_name","Employee_id","Group","Sub_Group","Contact_number","Working_For_Client","Client_Email_id","Client_Laptop","Client_Mouse","Client_Headphones","Client_Computer","Client_Remarks","BI_Email_id","BI_Laptop","BI_Mouse","BI_Headphones","BI_Computer","BI_Remarks"]

        widgets = {
            "Employee_name": forms.TextInput(attrs={'class':'form-control'}),
            "Employee_id": forms.TextInput(attrs={'class':'form-control'}),
            "Group": forms.TextInput(attrs={'class':'form-control'}),
            "Sub_Group" : forms.TextInput(attrs={'class':'form-control'}),
            "Contact_number" : forms.TextInput(attrs={'class':'form-control'}),
            "Working_For_Client" : forms.CheckboxInput(),
            "Client_Email_id" : forms.TextInput(attrs={'class':'form-control'}),
            "Client_Laptop" : forms.TextInput(attrs={'class':'form-control'}),
            "Client_Mouse" : forms.TextInput(attrs={'class':'form-control'}),
            "Client_Headphones" : forms.TextInput(attrs={'class':'form-control'}),
            "Client_Computer" : forms.TextInput(attrs={'class':'form-control'}),
            "Client_Remarks" : forms.TextInput(attrs={'class':'form-control'}),
            "BI_Email_id" : forms.TextInput(attrs={'class':'form-control'}),
            "BI_Laptop" : forms.TextInput(attrs={'class':'form-control'}),
            "BI_Mouse" : forms.TextInput(attrs={'class':'form-control'}),
            "BI_Headphones" : forms.TextInput(attrs={'class':'form-control'}),
            "BI_Computer" : forms.TextInput(attrs={'class':'form-control'}),
            "BI_Remarks": forms.TextInput(attrs={'class':'form-control'}),
        }