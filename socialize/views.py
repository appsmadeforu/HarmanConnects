from django.shortcuts import render, redirect
from socialize.forms import EmployeeSignupForm, ProjectDetailsForm
from socialize.models import Employee


def index(request):
    if request.user.id:
        employee = Employee.objects.get(id=request.user.id)
        return render(request, "index.html", {'employee': employee})
    else:
        return render(request, "index.html")



def signup(request):
    if request.method == 'POST':
        form = EmployeeSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeSignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def project(request):
    if request.method == 'POST':
        form = ProjectDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectDetailsForm()
    return render(request, 'projectDetails.html', {'form': form})

