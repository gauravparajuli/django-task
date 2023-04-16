from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    records = Employee.objects.all()
    return render(request, 'index.html', {'records': records})


def employee_delete(request, pk):
    try:
        emp = Employee.objects.get(id=pk)
        emp.delete()
        messages.info(request, 'Employee deleted!')
        return redirect('home')
    except ObjectDoesNotExist:
        messages.error(request, 'Employee not found!')
        return redirect('home')


def employee_update(request, pk):
    try:
        emp = Employee.objects.get(id=pk)
        emp.delete()
        messages.info(request, 'Employee deleted!')
        return redirect('home')
    except ObjectDoesNotExist:
        messages.error(request, 'Employee not found!')
        return redirect('home')
