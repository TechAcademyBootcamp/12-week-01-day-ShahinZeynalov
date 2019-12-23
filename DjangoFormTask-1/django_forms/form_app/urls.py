from django.urls import path
from .views import form,home

urlpatterns = [

    path('form/',form,name='form'),
    path('',home,name='home'),
]
