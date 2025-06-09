from django.urls import path
from principal import views

urlpatterns = [
    path('', views.saludo),
    path('saludo/<str:nombre>/', views.saludar_usuario),
    
]

