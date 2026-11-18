from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import resend
import logging
from .models import MensajeContacto, SolicitudPresupuesto
from . import presupuesto

logger = logging.getLogger(__name__)


def _clp(n):
    return '$' + f'{n:,}'.replace(',', '.')


def _enviar_correo(asunto, texto, reply_to):
    """Envía un correo a CONTACT_EMAIL vía Resend. Devuelve True si se envió."""
    try:
        resend.api_key = settings.RESEND_API_KEY
        logger.info(f"Enviando email via Resend desde {settings.DEFAULT_FROM_EMAIL} a {settings.CONTACT_EMAIL}")
        datos = {
            'from': settings.DEFAULT_FROM_EMAIL,
            'to': [settings.CONTACT_EMAIL],
            'subject': asunto,
            'text': texto,
        }
        try:
            validate_email(reply_to)
            datos['reply_to'] = reply_to
        except ValidationError:
            pass  # un correo de respuesta inválido no debe impedir recibir el mensaje
        result = resend.Emails.send(datos)
        logger.info(f"Resend result: {result}")
        return True
    except Exception as e:
        logger.error(f"Error enviando email via Resend: {e}", exc_info=True)
        return False


def inicio(request):
    return render(request, 'inicio.html')


def sobre_mi(request):
    return render(request, 'sobreMi.html')


def ciencia_datos(request):
    return render(request, 'cienciaDatos.html')


def proyectos(request):
    return render(request, 'proyectos.html')


def calculadora(request):
    return render(request, 'calculadora.html', {'catalogo': presupuesto.catalogo()})


@require_POST
def solicitar_presupuesto(request):
    # Campo trampa para bots: un usuario real nunca lo ve ni lo llena.
    if request.POST.get('website'):
        return JsonResponse({'ok': True})

    nombre = request.POST.get('nombre', '').strip()
    email = request.POST.get('email', '').strip()
    asunto = request.POST.get('asunto', '').strip()
    mensaje = request.POST.get('mensaje', '').strip()
    ids = request.POST.getlist('features')

    def error(texto):
        return JsonResponse({'ok': False, 'error': texto}, status=400)

    if not (nombre and email and asunto and mensaje):
        return error('Por favor completa todos los campos.')
    if len(nombre) > 100 or len(asunto) > 200 or len(mensaje) > 5000:
        return error('Alguno de los campos es demasiado largo.')
    try:
        validate_email(email)
    except ValidationError:
        return error('El correo electrónico no es válido.')

    # Los precios se recalculan aquí con el catálogo del servidor; no se confía en el navegador.
    elegidas, mensual, anual = presupuesto.calcular(ids)
    if not elegidas:
        return error('Selecciona al menos una funcionalidad para solicitar el presupuesto.')

    solicitud = SolicitudPresupuesto.objects.create(
        nombre=nombre,
        email=email,
        asunto=asunto,
        mensaje=mensaje,
        funcionalidades=[{'id': f['id'], 'name': f['name'], 'price': f['price']} for f in elegidas],
        total_mensual=mensual,
        total_primer_anio=anual,
    )

    detalle = '\n'.join(f"  - {f['name']} ({f['cat']}): {_clp(f['price'])}/mes" for f in elegidas)
    texto = (
        f'Nueva solicitud de presupuesto desde el portafolio\n\n'
        f'De: {nombre} <{email}>\n'
        f'Asunto: {asunto}\n\n'
        f'Mensaje:\n{mensaje}\n\n'
        f'Funcionalidades seleccionadas ({len(elegidas)}):\n{detalle}\n\n'
        f'Implementación inicial: {_clp(presupuesto.IMPLEMENTACION)}\n'
        f'Suscripción mensual: {_clp(mensual)}\n'
        f'Total primer año: {_clp(anual)}\n'
    )
    solicitud.correo_enviado = _enviar_correo(f'[Presupuesto] {asunto} — {nombre}', texto, email)
    solicitud.save(update_fields=['correo_enviado'])

    return JsonResponse({'ok': True})


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        asunto = request.POST.get('asunto', '').strip()
        mensaje = request.POST.get('mensaje', '').strip()

        if nombre and email and asunto and mensaje:
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                asunto=asunto,
                mensaje=mensaje,
            )
            _enviar_correo(
                f'[Portafolio] {asunto} — {nombre}',
                f'De: {nombre} <{email}>\n\n{mensaje}',
                email,
            )

            messages.success(request, '¡Mensaje enviado! Te responderé dentro de 24 horas hábiles.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor completa todos los campos.')

    return render(request, 'contacto.html')
