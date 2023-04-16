from django.contrib import messages
from django.shortcuts import render, redirect

from employees.forms import EmployeeForm
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
        form = EmployeeForm(request.POST or None, instance=emp)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.info(request, 'Employee updated!')
                return redirect('home')
        else:
            return render(request, 'employee_update.html', {'form': form})

        return render(request, 'employee_update.html', {'form': form})

    except ObjectDoesNotExist:
        messages.error(request, 'Employee not found!')
        return redirect('home')
