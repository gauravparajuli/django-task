from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ()

    firstname = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    lastname = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    dob = forms.DateField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Date of Birth  (YYYY-MM-DD)'}))
    salary = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Salary ($)'}))
