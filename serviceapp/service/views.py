from django.shortcuts import render
from .models import Service

# Create your views here.

def service(request):
    return render(request, 'service/service.html')

def acteur(request):
    return render(request, 'service/acteur.html')

def detail(request):
    return render(request, 'service/detail.html')

def carreleur(request):
    main_o = Service.objects.all()
    return render(request, 'service/carreleur.html', {'main_os': main_o})

def electricien(request):
    main_o = Service.objects.all()
    return render(request, 'service/electricien.html', {'main_os': main_o})

def menuisier(request):
    main_o = Service.objects.all()
    return render(request, 'service/menuisier.html', {'main_os': main_o})

def peintre(request):
    main_o = Service.objects.all()
    return render(request, 'service/peintre.html', {'main_os': main_o})

def plombier(request):
    main_o = Service.objects.all()
    return render(request, 'service/plombier.html', {'main_os': main_o})

def vitrier(request):
    main_o = Service.objects.all()
    return render(request, 'service/vitrier.html', {'main_os': main_o})