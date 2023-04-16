from django.shortcuts import render
from .models import Employee

# Create your views here.


def home(request):
    records = Employee.objects.all()
    return render(request, 'index.html', {'records': records})
