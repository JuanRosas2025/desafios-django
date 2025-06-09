from django.shortcuts import render

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django")

def saludar_usuario(request, nombre):
    return HttpResponse(f"hola {nombre}")

def numero(request, numero):
    return HttpResponse(f"Buenas, tu numero es {numero}")
# Create your views here.
