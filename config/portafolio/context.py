from django.contrib.staticfiles import finders
from django.templatetags.static import static
from django.urls import translate_url
from django.utils import translation

# CV por idioma. Si el archivo de un idioma aún no existe, el botón se oculta solo.
CV_POR_IDIOMA = {
    'es': 'docs/CV Simon Castillo 2026.pdf',
    'en': 'docs/CV Simon Castillo 2026 EN.pdf',
}


def idioma(request):
    actual = translation.get_language() or 'es'
    otro = 'en' if actual.startswith('es') else 'es'
    ruta_cv = CV_POR_IDIOMA.get(actual[:2], CV_POR_IDIOMA['es'])
    return {
        'lang_switch_code': otro,
        'lang_switch_url': translate_url(request.path, otro),
        'cv_url': static(ruta_cv) if finders.find(ruta_cv) else None,
    }
