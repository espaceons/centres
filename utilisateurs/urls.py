
from utilisateurs import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name="utilisateurs"

urlpatterns = [
    path('', views.Home, name='home'),

    path('register/',views.RegisterView, name='register'),
    path('login/', views.loginView, name='login'),
    path('profile/', views.ProfileView, name='profile'),
    path('editprofile/',views.profile_edit, name='editprofile'),
    path('logout/', views.logoutView, name='logout'),
    path('relations/', views.profileuserrelations, name='relations'),
    path('gallery/', views.profileusergallery, name='gallery'),
    path('newfeed/', views.profileusernewfeed, name='newfeed'),
    
]

