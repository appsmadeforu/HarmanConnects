from django.shortcuts import render, redirect
from socialize.forms import EmployeeSignupForm, ProjectDetailsForm


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == 'POST':
        form = EmployeeSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
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
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpUser(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             emp_id = form.cleaned_data.get('emp_id')
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('first_name')
#             email = form.cleaned_data.get('email')
#             new_user = SignUpUser.objects.create(username, first_name, last_name, emp_id, email, raw_password, )
#             user = authenticate(username=username, password=raw_password, emp_id=emp_id, )
#             new_user.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpUser()
#     return render(request, 'registration/signup.html', {'form': form})
