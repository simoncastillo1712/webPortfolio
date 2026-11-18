from django.urls import path
from django.utils.functional import lazy
from django.utils.translation import get_language

from . import views

# Cada ruta tiene su versión en inglés. La ruta se resuelve según el idioma activo
# (español sin prefijo, inglés bajo /en/), sin depender de catálogos de traducción.
SLUGS_EN = {
    'sobre-mi/': 'about/',
    'ciencia-de-datos/': 'data-science/',
    'proyectos/': 'projects/',
    'contacto/': 'contact/',
    'calculadora/': 'quote/',
    'calculadora/solicitar/': 'quote/request/',
}


def ruta(es):
    def segun_idioma():
        return SLUGS_EN[es] if (get_language() or 'es').startswith('en') else es
    return lazy(segun_idioma, str)()


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path(ruta('sobre-mi/'), views.sobre_mi, name='sobre_mi'),
    path(ruta('ciencia-de-datos/'), views.ciencia_datos, name='ciencia_datos'),
    path(ruta('proyectos/'), views.proyectos, name='proyectos'),
    path(ruta('contacto/'), views.contacto, name='contacto'),
    path(ruta('calculadora/'), views.calculadora, name='calculadora'),
    path(ruta('calculadora/solicitar/'), views.solicitar_presupuesto, name='solicitar_presupuesto'),
]
