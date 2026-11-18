from django.db import models


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'

    def __str__(self):
        return f'{self.nombre} — {self.asunto}'


class SolicitudPresupuesto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    funcionalidades = models.JSONField(default=list)
    total_mensual = models.PositiveIntegerField()
    total_primer_anio = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    correo_enviado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Solicitud de presupuesto'
        verbose_name_plural = 'Solicitudes de presupuesto'

    def __str__(self):
        return f'{self.nombre} — {self.asunto}'
