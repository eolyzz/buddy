from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'homepage'),
    
    #registration
    path('accounts/', include('allauth.urls')),

    path('register_user/',views.register_user, name = 'signup'),
    #signup
    path('accounts/signup/',views.signup_user, name = 'signup'),
    #signedup check your mailbox

    #verify your mail

    #email verified

    #login
    path('accounts/login/',views.login_user, name = 'login'),
    path("logout_user/",views.logout_user, name = 'logout'),
     #dashboard
    path('dashboard/',views.dashboard, name = 'dashboard'),
]
#handler404 = "buddyapp.views.handle_not_found"
    

