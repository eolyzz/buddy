from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', views.homepage, name = 'homepage'),
    #registration
    #signup
    #signedup check your mailbox
    #verify your mail
    #email verified
    #dashboard
    #login
]
