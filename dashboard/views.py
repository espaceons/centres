from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request,'dashboard/home.html', context)


def administrations(request):
    context = {}
    return render(request,'centres/administrations.html', context)


def detailadmin(request):
    context= {}
    return render(request,'centres/detailadministrations.html', context)
