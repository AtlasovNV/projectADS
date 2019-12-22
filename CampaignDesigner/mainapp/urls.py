from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('campaign/create/', mainapp.campaign_create, name='campaign_create'),
    path('campaign/create/<int:pk>/first/', mainapp.first_page,
         name='first_page'),
    path('campaign/create/<int:pk>/second/', mainapp.second_page,
         name='second_page'),
    path('campaign/create/<int:pk>/third/', mainapp.third_page,
         name='third_page'),
    path('campaing/create/<int:pk>/finish/', mainapp.fourth_page,
         name='fourth_page'),
    path('campaing/<int:pk>/download/xls', mainapp.download_xls,
         name='download_xls'),
]
