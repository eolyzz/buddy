from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('accounts/login/', views.login_api),
    path('accounts/user/', views.get_user_data),
    path('accounts/register/', views.register_api),
    path('accounts/logout/', knox_views.LogoutView.as_view()),
    path('accounts/logoutall/', knox_views.LogoutView.as_view()),
]