from django.contrib import admin
from .models import MainDashBoard, Employee, Asset_Allocation


class Asset_Allocation_FormAdmin(admin.ModelAdmin):
    list_display = "Employee_name", "Employee_id", "Group", "Sub_Group", "Working_For_Client", "Employee_Status"
admin.site.register(Asset_Allocation, Asset_Allocation_FormAdmin)
class MainDashBoardAdmin(admin.ModelAdmin):
    list_display = "s_no","Catagory_name"
admin.site.register(MainDashBoard,MainDashBoardAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = "employeename","employeeid","assetid","gender","start_date","end_date"

admin.site.register(Employee,EmployeeAdmin)


