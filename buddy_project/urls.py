from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #registration
    path('register_user/',views.register_user, name = 'signup'),
    #signup
    path('signup_user/',views.signup_user, name = 'signup'),
    #signedup check your mailbox

    #verify your mail

    #email verified

    #login
    path('login_user/',views.login_user, name = 'login'),
    path("logout_user/",views.logout_user, name = 'logout'),
     #dashboard
    path('dashboard/',views.dashboard, name = 'dashboard'),
   
    
]
handler404 = "buddy_project.views.handle_not_found"