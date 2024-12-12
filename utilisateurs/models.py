from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 


from param.models import Centre, Role
class CustonUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email non vallide')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
    



class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=180, blank=True)
    last_name = models.CharField(max_length=180, blank=True)
    email = models.EmailField(unique=True)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    
    objects = CustonUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
    
    
    
    
    
    

class userProfile(models.Model):
    user = models.OneToOneField( CustomUser, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    PHOTO = models.ImageField(upload_to='utilisateurs/imgavatar', blank=True, null=True)

    

    def __str__(self):
        return self.user.username
