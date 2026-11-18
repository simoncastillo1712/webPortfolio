"""Catálogo de la calculadora de presupuesto.

Única fuente de verdad: la página lo entrega al navegador (json_script) y el
servidor lo usa para recalcular los precios de cada solicitud, sin confiar en
los valores que envía el cliente.
"""

IMPLEMENTACION = 350000

FEATURES = [
    # --- Contenido y administración ---
    {'id': 'cms',       'cat': 'Contenido y administración', 'name': 'Panel CMS',          'desc': 'Editor visual para que el cliente actualice sin tocar código', 'price': 18000},
    {'id': 'blog',      'cat': 'Contenido y administración', 'name': 'Blog / noticias',    'desc': 'Publicaciones con categorías, etiquetas y SEO básico',         'price': 12000},
    {'id': 'gallery',   'cat': 'Contenido y administración', 'name': 'Galería multimedia', 'desc': 'Imágenes y videos optimizados con gestor de archivos',         'price': 10000},
    {'id': 'multilang', 'cat': 'Contenido y administración', 'name': 'Multi-idioma (i18n)', 'desc': 'Versiones del sitio en más de un idioma con cambio dinámico', 'price': 22000},

    # --- E-commerce y pagos ---
    {'id': 'cart',         'cat': 'E-commerce y pagos', 'name': 'Carro de compras',      'desc': 'Gestión de productos, stock y órdenes',                  'price': 35000},
    {'id': 'payment',      'cat': 'E-commerce y pagos', 'name': 'Pasarela de pago (API)', 'desc': 'Integración con Transbank, MercadoPago, Stripe u otro', 'price': 28000},
    {'id': 'clientportal', 'cat': 'E-commerce y pagos', 'name': 'Portal de clientes',    'desc': 'Login, historial de compras y seguimiento de pedidos',   'price': 22000},
    {'id': 'coupons',      'cat': 'E-commerce y pagos', 'name': 'Cupones y descuentos',  'desc': 'Códigos promocionales y precios dinámicos',              'price': 15000},

    # --- Reservas y agenda ---
    {'id': 'booking',   'cat': 'Reservas y agenda', 'name': 'Sistema de reservas',         'desc': 'Calendario con disponibilidad y confirmación automática', 'price': 25000},
    {'id': 'recurring', 'cat': 'Reservas y agenda', 'name': 'Pago recurrente / membresía', 'desc': 'Cobro mensual automático a suscriptores',                 'price': 28000},

    # --- Automatización e IA ---
    {'id': 'chatbot',       'cat': 'Automatización e IA', 'name': 'Chatbot con IA',             'desc': 'Asistente conversacional entrenado con info del negocio', 'price': 45000},
    {'id': 'smartform',     'cat': 'Automatización e IA', 'name': 'Formularios inteligentes',   'desc': 'Lógica condicional, validación y envío a CRM o email',    'price': 12000},
    {'id': 'notifications', 'cat': 'Automatización e IA', 'name': 'Notificaciones automáticas', 'desc': 'Emails y/o WhatsApp automáticos por eventos del sitio',   'price': 18000},

    # --- Analytics y SEO ---
    {'id': 'analytics', 'cat': 'Analytics y SEO', 'name': 'Dashboard de analytics', 'desc': 'Visitas, conversiones y métricas clave del negocio',        'price': 15000},
    {'id': 'seo',       'cat': 'Analytics y SEO', 'name': 'SEO técnico',            'desc': 'Meta tags, sitemap, Schema.org y velocidad de carga',       'price': 15000},
    {'id': 'reports',   'cat': 'Analytics y SEO', 'name': 'Reportes mensuales',     'desc': 'Informe PDF automático con resumen de tráfico y métricas', 'price': 12000},

    # --- Infraestructura ---
    {'id': 'hosting', 'cat': 'Infraestructura', 'name': 'Hosting + dominio gestionado', 'desc': 'Gestión de servidor, SSL y renovación de dominio',            'price': 20000},
    {'id': 'support', 'cat': 'Infraestructura', 'name': 'Soporte y mantención',         'desc': 'Corrección de bugs, actualizaciones y soporte hasta 3h/mes', 'price': 30000},
    {'id': 'backup',  'cat': 'Infraestructura', 'name': 'Backup automático',            'desc': 'Copias de seguridad diarias con restauración en 24h',        'price': 12000},
]

PACKS = {
    'vitrina':      {'label': 'Comercio pequeño', 'features': ['cms', 'smartform', 'seo', 'hosting', 'support']},
    'ecommerce':    {'label': 'E-commerce',       'features': ['cart', 'payment', 'clientportal', 'coupons', 'notifications', 'analytics', 'hosting', 'support', 'backup']},
    'restaurante':  {'label': 'Restaurante',      'features': ['cms', 'booking', 'gallery', 'notifications', 'seo', 'hosting', 'support']},
    'clinica':      {'label': 'Clínica / Médico', 'features': ['booking', 'clientportal', 'chatbot', 'payment', 'notifications', 'blog', 'seo', 'hosting', 'support', 'backup']},
    'gym':          {'label': 'Gym / Deportivo',  'features': ['cart', 'payment', 'recurring', 'clientportal', 'notifications', 'gallery', 'cms', 'hosting', 'support']},
    'inmobiliaria': {'label': 'Inmobiliaria',     'features': ['cms', 'chatbot', 'smartform', 'gallery', 'notifications', 'blog', 'seo', 'hosting', 'support', 'backup']},
}

FEATURES_POR_ID = {f['id']: f for f in FEATURES}


def catalogo():
    return {'features': FEATURES, 'packs': PACKS, 'implementacion': IMPLEMENTACION}


def calcular(ids):
    """Devuelve (funcionalidades, total_mensual, total_primer_anio) a partir de ids válidos.

    Ignora ids desconocidos y duplicados; el orden es el del catálogo.
    """
    elegidas = [f for f in FEATURES if f['id'] in set(ids)]
    mensual = sum(f['price'] for f in elegidas)
    return elegidas, mensual, IMPLEMENTACION + mensual * 12
