from django.contrib import admin
from utilisateurs.models import CustomUser, CustomUserProfile



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone', 'centre', 'role', 'is_active']
    
class CustomUserProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'photo', 'description', 'verified']
    


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUserProfile, CustomUserProfileAdmin)