from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ()

    firstname = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Date of Birth  (YYYY-MM-DD)'}))
    salary = forms.IntegerField(label='Salary', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Salary ($)'}))
