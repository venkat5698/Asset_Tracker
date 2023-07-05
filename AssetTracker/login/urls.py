from django.urls import path
from . import views

urlpatterns=[
    path("/",views.loginpage, name="loginpage"),
    path("/password/",views.forgotpasswordpage, name="forgotpasswordpage"),
    path("/register/",views.registerpage, name="registerpage"),
]