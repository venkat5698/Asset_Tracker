from django.urls import path

from . import views
from .views import *
from .views import AssetFormView

urlpatterns = [
    path("", home, name="home"),
    path('dashboard/', dashboard, name='dashboard'),
    path("table", table, name="table"),
    path("register",register, name="register"),
    path('addProduct/',add_details, name='addProduct' ),
    path('clientreport/', NewJoinerreport, name='clientreport' ),
    path('asseetform/', Asseetform, name='asseetform' ),
    path('submit/', submit_form, name='submit_form'),
    path('Assetform/', AssetFormView, name='asset_form'),
    path('success/', success, name='success'),

]


