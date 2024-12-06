from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("veiller inserrez email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(rself, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")
        
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return rself.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = (
        (1,'Formateur'),
        (2,'Conseiller'),
        (3,'Directeur'),
        (4,'Coordinateur'),
        (5,'RS'),
        (6,'RAF'),
        (7,'FC'),
        (8,'TPRO'),
        (9,'Entreprise'),
        (10,'Dregional'),
        (11,'Visiteur'),
        (12,'Apprentis'),
        
    )
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    role = models.SmallIntegerField(choices=ROLE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, perm, obj=None):
        return True