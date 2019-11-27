from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('first/', mainapp.first_page, name='first_page'),
    path('second/', mainapp.second_page, name='second_page'),
]