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


class IdiomaTests(TestCase):
    PAGINAS = [
        ('inicio', 'inicio', 'Home'),
        ('sobre_mi', 'sobre-mi', 'About me'),
        ('ciencia_datos', 'ciencia-de-datos', 'Data Science'),
        ('proyectos', 'proyectos', 'Featured Projects'),
        ('contacto', 'contacto', 'Send me a message'),
        ('calculadora', 'calculadora', 'Request a quote'),
    ]

    def test_todas_las_paginas_cargan_en_ambos_idiomas(self):
        from django.utils import translation
        for nombre, _slug, texto_en in self.PAGINAS:
            with translation.override('es'):
                url_es = reverse(nombre)
            with translation.override('en'):
                url_en = reverse(nombre)
            self.assertFalse(url_es.startswith('/en/'), url_es)
            self.assertTrue(url_en.startswith('/en/'), url_en)

            r_es = self.client.get(url_es)
            self.assertEqual(r_es.status_code, 200, url_es)
            self.assertContains(r_es, '<html lang="es">')

            r_en = self.client.get(url_en)
            self.assertEqual(r_en.status_code, 200, url_en)
            self.assertContains(r_en, '<html lang="en">')
            self.assertContains(r_en, texto_en)

    def test_el_selector_de_idioma_lleva_a_la_misma_pagina(self):
        r = self.client.get('/proyectos/')
        self.assertContains(r, 'href="/en/projects/"')
        r = self.client.get('/en/projects/')
        self.assertContains(r, 'href="/proyectos/"')

    def test_el_catalogo_de_la_calculadora_se_entrega_en_ingles(self):
        r = self.client.get('/en/quote/')
        self.assertContains(r, 'Shopping cart')
        self.assertNotContains(r, 'Carro de compras')
        r = self.client.get('/calculadora/')
        self.assertContains(r, 'Carro de compras')

    def test_la_pagina_en_ingles_no_deja_textos_en_espanol(self):
        for ruta in ['/en/', '/en/about/', '/en/data-science/', '/en/projects/', '/en/contact/', '/en/quote/']:
            html = self.client.get(ruta).content.decode()
            for palabra in ['Proyectos Destacados', 'Sobre mí', 'Descargar CV', 'Solicitar presupuesto', 'Ver repositorio']:
                self.assertNotIn(palabra, html, f'{palabra} en {ruta}')

    def test_el_boton_de_cv_en_ingles_aparece_solo_si_existe_el_archivo(self):
        from django.contrib.staticfiles import finders
        existe = bool(finders.find('docs/CV Simon Castillo 2026 EN.pdf'))
        html = self.client.get('/en/about/').content.decode()
        self.assertEqual('Download CV' in html, existe)
        self.assertIn('Descargar CV', self.client.get('/sobre-mi/').content.decode())

    @patch('portafolio.views.resend.Emails.send')
    def test_solicitud_en_ingles_devuelve_errores_en_ingles(self, send):
        r = self.client.post('/en/quote/request/', {'nombre': 'A', 'email': 'a@b.cl', 'asunto': 'x', 'mensaje': 'y'})
        self.assertEqual(r.status_code, 400)
        self.assertIn('Select at least one feature', r.json()['error'])
        r = self.client.post('/quote/request/', {})
        self.assertEqual(r.status_code, 404)  # la ruta en español no existe bajo ese nombre

    @patch('portafolio.views.resend.Emails.send')
    def test_correo_al_dueno_indica_el_idioma_del_visitante(self, send):
        self.client.post('/en/quote/request/', {
            'nombre': 'Jane', 'email': 'jane@example.com', 'asunto': 'Site', 'mensaje': 'Hi',
            'features': ['cms'],
        })
        texto = send.call_args[0][0]['text']
        self.assertIn('Idioma del sitio: English', texto)
        self.assertIn('Panel CMS', texto)  # el correo a Simón va siempre en español
