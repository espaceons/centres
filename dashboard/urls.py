
from dashboard import views
from django.urls import path


app_name='dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('administrations/', views.administrations, name='administrations'),
    path('detailadmin/', views.detailadmin, name='detailadmin'),
]