
from utilisateurs import forms
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from utilisateurs.models import *
from django.contrib.auth import authenticate, login, logout


def logoutView(request):
    logout(request)
    return redirect('vitrine:index')




def loginView(request):
    form = forms.LoginViewForm()
    message=''
    if request.method == 'POST':
        form = forms.LoginViewForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                message = f'bienvenue , { user.username } ! au site du centre'
                context = {
                    'user':user,
                    'message': message,
                }
                return redirect('dashboard:home')
            else:
                message = 'Identifiant non valid'
    context ={
        'form':form,
        'message':message,
    }
    return render(request, 'utilisateur/login.html', context)






def RegisterView(request):
    return render(request, 'utilisateur/register.html')