from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
#from django.utils.encoding import force_bytes,force_str,force_text, DjangoUnicodeDecodeError




def homepage (request):
    return render (request, 'homepage.html', {})

def register_user (request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
          #  send_action_email(user, request)

            return redirect ('login')
    else:
        form = CreateUserForm()
    context = {
                'form':form
                }
    return render (request, 'registerPage.html', context)

def login_user (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if not user.is_email_verified:
            messages.add_message (request, messages.error,
            "Email is not verified, Please check your inbox"),
            return render (request, 'login.html')

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
    return render (request, 'loginPage.html', context)
def signup_user (request):
    return render (request, 'registerPage.html')

def dashboard(request):
    return render (request, 'dashboard.html')

def logout_user (request):
        logout (request)
        return redirect("login")