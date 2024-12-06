from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'vitrine/index.html')


def abonnezvous(request):
    return render(request,'vitrine/abonnezvous.html')


def admissions(request):
    return render(request,'vitrine/admissions.html')

def cours(request):
    return render(request,'vitrine/cours.html')

def coursesingle(request):
    return render(request,'vitrine/coursesingle.html')

def about(request):
    return render(request,'vitrine/about.html')

def formateur(request):
    return render(request,'vitrine/formateurs.html')
