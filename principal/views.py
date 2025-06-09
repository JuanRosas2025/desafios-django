from django.shortcuts import render

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django \n Jp si ves esto si funciono")

def saludar_usuario(request, nombre):
    return HttpResponse(f"hola {nombre}")

# Create your views here.
