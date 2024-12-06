from django.contrib import admin

import utilisateurs
from utilisateurs.models import CustomUser


admin.site.register(CustomUser)