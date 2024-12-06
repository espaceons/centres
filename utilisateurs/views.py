from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from utilisateurs.models import *

def loginView(request):
    return render(request, 'utilisateur/login.html')

def RegisterView(request):
    return render(request, 'utilisateur/register.html')