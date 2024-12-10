from django.contrib import admin
import utilisateurs
from utilisateurs.models import CustomUser, userProfile


admin.site.register(CustomUser)

admin.site.register(userProfile)