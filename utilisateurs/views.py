
from utilisateurs import forms
from django.shortcuts import get_object_or_404, render,redirect
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
from utilisateurs.forms import RegisterViewForm
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




@login_required(login_url='/accounts/login/')
def ProfileView(request):
    profile = CustomUserProfile.objects.all()
    context = {
        'profile':profile,
    }
    return render(request,'dashboard/profile.html', context)



@login_required(login_url='/accounts/login/')
def profile_edit(request):
    context = {}
    return render(request,'dashboard/profileuseredit.html', context)





@login_required(login_url='/accounts/login/')
def profileuserrelations(request):
    context= {}
    return render(request,'dashboard/profileuserrelations.html', context)

@login_required(login_url='/accounts/login/')
def profileusergallery(request):
    context= {}
    return render(request,'dashboard/profileusergallery.html', context)



@login_required(login_url='/accounts/login/')
def profileusernewfeed(request):
    context= {}
    return render(request,'dashboard/profileusernewfeed.html', context)



        