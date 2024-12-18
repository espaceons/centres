from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    context = {}
    return render(request,'dashboard/home.html', context)

@login_required(login_url='/accounts/login/')
def administrations(request):
    context = {}
    return render(request,'centres/administrations.html', context)

@login_required(login_url='/accounts/login/')
def detailadmin(request):
    context= {}
    return render(request,'centres/detailadministrations.html', context)