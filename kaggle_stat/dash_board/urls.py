from django.urls import path
from . import views


app_name = 'statistics'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard_list, name='dashboard_list'),
    path('dashboard/<slug:dashboard_slug>', views.dashboard_detail, name='dashboard_detail')
]
