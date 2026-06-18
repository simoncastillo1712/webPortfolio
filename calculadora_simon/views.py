# views.py
# Añade esta función a tu views.py existente

from django.shortcuts import render


def calculadora(request):
    """Vista de la calculadora de presupuesto web."""
    return render(request, 'calculadora.html')
