
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone
from param.models import Centre, Role
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
        
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def __str__(self):
        return self.username
    
    


class CustomUserProfile(models.Model):
    user = models.OneToOneField( CustomUser, on_delete=models.CASCADE, related_name='userprofile')
    username = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='utilisateurs/imgavatar/', blank=True, null=True)
    verified = models.BooleanField(default=False) 

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = CustomUserProfile(user=instance)
        user_profile.save()
        
#post_save.connect(create_profile, sender=CustomUser)// remplacer par @receiver(post_save, sender=CustomUser)
        