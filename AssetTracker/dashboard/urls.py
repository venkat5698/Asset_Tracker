from django.urls import path
from . import views

urlpatterns=[
    path("/",views.dashboardpage, name="dashboardpage"),
    path("/layout-static",views.layoutpage, name="layoutpage"),
]