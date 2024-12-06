
from vitrine import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name='vitrine'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('formateur/', views.formateur, name='formateur'),
    path('admissions/', views.admissions, name='admissions'),
    path('abonnezvous/', views.abonnezvous, name='abonnezvous'),
    path('cours/', views.cours, name='cours'),
    path('coursesingle/', views.coursesingle, name='coursesingle'),
    
]

