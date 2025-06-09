from django.urls import path
from principal import views

urlpatterns = [
    path('', views.saludo),
    path('saludame/<str:nombre>/', views.saludar_usuario),
    path('numero/<int:numero>/', views.numero),
    
]

