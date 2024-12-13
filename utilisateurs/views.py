
from utilisateurs import forms
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse
from utilisateurs.models import *
from utilisateurs.forms import RegisterViewForm, userUpdateForm
from django.contrib.auth import authenticate, login, logout


# logout

def logoutView(request):
    logout(request)
    return redirect('vitrine:index')

# login

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




# enregistrement

def RegisterView(request):
    if request.method == 'POST':
        form = RegisterViewForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            context = {
            'new_user':new_user,
        }
            return render(request, 'utilisateur/login.html', context)
    else:
        form = RegisterViewForm()
    context = {
        'form':form,
    }
    return render(request, 'utilisateur/register.html', context)





def Home(request):
    return render(request, 'vitrine/index.html')


def CustomUserProfileViews(request, username):
    if request.method == 'POST':
        user = request.user
        form = userUpdateForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request,f'{user_form.username}, votre profile est mis a jour !')
            return redirect("profile", user_form.username)
        
    user = CustomUser.objects.filter(usrname=username).first()
    if user:
        form = userUpdateForm(isinstance=user)
        context = {
            'form':form,
            }
        return render( request, 'utilisateurs:CustomUserProfileViews', context)
    return redirect('dashboard/home.html')
        