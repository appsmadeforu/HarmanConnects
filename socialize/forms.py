from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput

from socialize.models import Employee, Project


class EmployeeSignupForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = ('emp_id', 'username', 'first_name', 'last_name', 'dob', 'email', 'password1', 'password2',)
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }


class ProjectDetailsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('proj_name', 'proj_link', 'proj_description', 'proj_start_date')
        widgets = {
            'proj_start_date': DateInput(attrs={'type': 'date'})
        }