from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/delete/<int:pk>/', views.employee_delete, name='delete'),
    path('employee/update/<int:pk>/', views.employee_update, name='update')
]
