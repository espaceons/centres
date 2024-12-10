
from utilisateurs import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name='utilisateur'

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('profile/', views.userProfile, name='profile'),
    path('logout/', views.logoutView, name='logout'),
    path('register/',views.RegisterView, name='register'),
]

