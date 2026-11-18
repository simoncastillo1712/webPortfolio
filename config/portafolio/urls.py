from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('ciencia-de-datos/', views.ciencia_datos, name='ciencia_datos'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('calculadora/solicitar/', views.solicitar_presupuesto, name='solicitar_presupuesto'),
]