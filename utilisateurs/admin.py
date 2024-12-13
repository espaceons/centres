from django.contrib import admin
from utilisateurs.models import CustomUser, CustomUserProfile


admin.site.register(CustomUser)
admin.site.register(CustomUserProfile)