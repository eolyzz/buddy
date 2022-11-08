from urllib import request
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import Members

# Create your views here.
def register_user(request):
    return render (request, 'register_user.html')
def signup_user (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    else:
        form = CreateUserForm()
    context = {
                'form':form
                }
    return render (request, 'authenticate/register.html', context)
            

def login_user (request):
  #  form = CreateUserForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
        
    else:
        # Return an 'invalid login' error message.
        form = CreateUserForm()
    context = {
                'form':form
                }
    return render (request, 'authenticate/login.html', context)
    


def logout_user (request):
        logout (request)
        return redirect("login")

@login_required(login_url="login")
def dashboard (request):
    members = Members.objects.all().order_by('name')
    context = {'members': members}
    return render (request, 'dashboard.html', context)
"""
    MembersForm = MembersForm(instance=request.user.profile)
    context = {
        'MembersForm':MembersForm
    }
"""

def handle_not_found (request, exception):
    return redirect('homepage')