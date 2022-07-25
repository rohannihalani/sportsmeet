from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.auth, name="auth_choice-page"),
    path('login/', views.login_request, name="login-page"),
    path('signup/', views.register_request, name="signup-page"),
    path('profile/', views.profile, name="profile-page"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout-page")


]