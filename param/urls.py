
from django.urls import path

from param import views

app_name='param'

urlpatterns = [

    path('centre/create/',views.create_centre, name='creation'),
    path('centre/liste/',views.liste_centre, name='liste'),
    path('centre/update/<int:pk>', views.update_centre, name= 'update'),
    path('centre/delete/<int:pk>', views.delete_centre, name= 'delete'),
]

