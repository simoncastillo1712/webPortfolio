# urls.py
# Añade esta línea a tu urlpatterns existente

from django.urls import path
from . import views  # ajusta el import según tu estructura

urlpatterns = [
    # ... tus URLs existentes ...

    path('calculadora/', views.calculadora, name='calculadora'),
]
