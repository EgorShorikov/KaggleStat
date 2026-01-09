from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'dash_board'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<slug:dashboard_slug>', views.dashboard, name='dashboard')
]
