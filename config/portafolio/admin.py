from django.contrib import admin
from .models import MensajeContacto, SolicitudPresupuesto


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'fecha', 'leido')
    list_filter = ('leido', 'fecha')
    search_fields = ('nombre', 'email', 'asunto')
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'fecha')


@admin.register(SolicitudPresupuesto)
class SolicitudPresupuestoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'total_mensual', 'fecha', 'leido', 'correo_enviado')
    list_filter = ('leido', 'correo_enviado', 'fecha')
    search_fields = ('nombre', 'email', 'asunto')
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'funcionalidades',
                       'total_mensual', 'total_primer_anio', 'fecha', 'correo_enviado')
