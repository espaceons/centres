
from utilisateurs import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name='utilisateur'

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('register/',views.RegisterView, name='register')
]

