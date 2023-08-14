from datetime import datetime

from django.db import models
from rest_framework.exceptions import ValidationError


class MainDashBoard(models.Model):
    s_no = models.IntegerField(blank=False,null=False)
    Catagory_name = models.CharField(max_length=100,blank=False,null=False)
    #is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.Catagory_name
class Asset_Allocation(models.Model):
    Employee_name = models.CharField(max_length=100, blank=False, null=False)
    Employee_id = models.CharField(max_length=100, blank=False,null=False)
    Group = models.CharField(max_length=100, blank=False,null=False)
    Sub_Group = models.CharField(max_length=100, blank=False, null=False)
    Contact_number = models.CharField(max_length=50, blank=False, null=False)
    Working_For_Client = models.BooleanField(default=True)
    Client_Email_id = models.CharField(max_length=100, blank=False,null=False)
    Client_Laptop = models.CharField(max_length=100, blank=False,null=False)
    Client_Mouse = models.CharField(max_length=100, blank=False, null=False)
    Client_Headphones = models.CharField(max_length=100, blank=False, null=False)
    Client_Computer = models.CharField(max_length=100, blank=False, null=False)
    Client_Remarks = models.CharField(max_length=200, blank=False, null=False)
    Employee_Status = models.ForeignKey(MainDashBoard, on_delete=models.CASCADE, default=True, null=True)
    BI_Email_id = models.CharField(max_length=100, blank=False, null=False)
    BI_Laptop = models.CharField(max_length=100, blank=False, null=False)
    BI_Mouse = models.CharField(max_length=100, blank=False, null=False)
    BI_Headphones = models.CharField(max_length=100, blank=False, null=False)
    BI_Computer = models.CharField(max_length=100, blank=False, null=False)
    BI_Remarks = models.CharField(max_length=200, blank=False, null=True)
    # Employee_Exit_Date = models.DateTimeField(default=True, null=True)
    def __str__(self):
        return self.Employee_id

    def is_valid(self):
        # Perform custom validation for the model instance
        try:
            self.full_clean()
            return True
        except ValidationError:
            return False


class Employee(models.Model):
    employeename = models.CharField(max_length=100, blank=False, null=False)
    employeeid = models.CharField(max_length=20, blank=False, null=False)
    assetid = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')])
    start_date = models.DateField()
    end_date = models.DateField()
    #filename = models.FileField(upload_to='uploads/') # This will save the uploaded file to the 'uploads/' directory.

    def __str__(self):
        return str(self.employeename)





