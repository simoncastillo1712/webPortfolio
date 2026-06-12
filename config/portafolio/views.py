from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import MensajeContacto


def inicio(request):
    return render(request, 'inicio.html')


def sobre_mi(request):
    return render(request, 'sobreMi.html')


def proyectos(request):
    return render(request, 'proyectos.html')


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
            try:
                send_mail(
                    subject=f'[Portafolio] {asunto} — {nombre}',
                    message=f'De: {nombre} <{email}>\n\n{mensaje}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception:
                pass  # El mensaje ya quedó guardado en BD

            messages.success(request, '¡Mensaje enviado! Te responderé dentro de 24 horas hábiles.')
            return redirect('contacto')
        else:
            messages.error(request, 'Por favor completa todos los campos.')

    return render(request, 'contacto.html')
