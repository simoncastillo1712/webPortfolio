from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from .models import SolicitudPresupuesto
from . import presupuesto


class SolicitarPresupuestoTests(TestCase):
    def setUp(self):
        self.url = reverse('solicitar_presupuesto')
        self.datos = {
            'nombre': 'Ana Pérez',
            'email': 'ana@example.com',
            'asunto': 'Sitio para mi tienda',
            'mensaje': 'Necesito vender online.',
            'features': ['cart', 'payment'],
        }

    def test_la_pagina_entrega_el_catalogo_y_el_boton_deshabilitado(self):
        r = self.client.get(reverse('calculadora'))
        self.assertContains(r, 'id="catalogo-data"')
        self.assertContains(r, 'id="btn-solicitar"')

    @patch('portafolio.views.resend.Emails.send')
    def test_guarda_y_envia_correo_con_precios_del_servidor(self, send):
        # El cliente no puede alterar los precios: se recalculan en el servidor.
        datos = {**self.datos, 'precio': '1', 'total_mensual': '1'}
        r = self.client.post(self.url, datos)
        self.assertEqual(r.status_code, 200)
        self.assertTrue(r.json()['ok'])

        s = SolicitudPresupuesto.objects.get()
        self.assertEqual(s.total_mensual, 35000 + 28000)
        self.assertEqual(s.total_primer_anio, presupuesto.IMPLEMENTACION + 63000 * 12)
        self.assertTrue(s.correo_enviado)

        payload = send.call_args[0][0]
        self.assertEqual(payload['reply_to'], 'ana@example.com')
        self.assertIn('Carro de compras', payload['text'])
        self.assertIn('Pasarela de pago', payload['text'])
        self.assertIn('Necesito vender online.', payload['text'])

    def test_sin_funcionalidades_es_rechazada(self):
        r = self.client.post(self.url, {**self.datos, 'features': []})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(SolicitudPresupuesto.objects.count(), 0)

    def test_ids_desconocidos_se_ignoran(self):
        r = self.client.post(self.url, {**self.datos, 'features': ['inventado']})
        self.assertEqual(r.status_code, 400)

    def test_email_invalido_o_campos_vacios(self):
        self.assertEqual(self.client.post(self.url, {**self.datos, 'email': 'no-es-email'}).status_code, 400)
        self.assertEqual(self.client.post(self.url, {**self.datos, 'nombre': ''}).status_code, 400)

    @patch('portafolio.views.resend.Emails.send')
    def test_honeypot_no_guarda_ni_envia(self, send):
        r = self.client.post(self.url, {**self.datos, 'website': 'http://spam'})
        self.assertTrue(r.json()['ok'])
        self.assertEqual(SolicitudPresupuesto.objects.count(), 0)
        send.assert_not_called()

    @patch('portafolio.views.resend.Emails.send', side_effect=Exception('fallo de Resend'))
    def test_si_falla_el_correo_la_solicitud_queda_guardada(self, send):
        r = self.client.post(self.url, self.datos)
        self.assertTrue(r.json()['ok'])
        self.assertFalse(SolicitudPresupuesto.objects.get().correo_enviado)

    def test_solo_acepta_post(self):
        self.assertEqual(self.client.get(self.url).status_code, 405)
