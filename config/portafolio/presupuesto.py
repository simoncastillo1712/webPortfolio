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


# Textos en inglés del catálogo, por id de funcionalidad.
FEATURES_EN = {
    'cms':           ('Content & administration', 'CMS panel',                  'Visual editor so the client can update content without touching code'),
    'blog':          ('Content & administration', 'Blog / news',                'Posts with categories, tags and basic SEO'),
    'gallery':       ('Content & administration', 'Media gallery',              'Optimized images and videos with a file manager'),
    'multilang':     ('Content & administration', 'Multi-language (i18n)',      'Site versions in more than one language with dynamic switching'),
    'cart':          ('E-commerce & payments',    'Shopping cart',              'Product, stock and order management'),
    'payment':       ('E-commerce & payments',    'Payment gateway (API)',      'Integration with Transbank, MercadoPago, Stripe or others'),
    'clientportal':  ('E-commerce & payments',    'Customer portal',            'Login, purchase history and order tracking'),
    'coupons':       ('E-commerce & payments',    'Coupons & discounts',        'Promo codes and dynamic pricing'),
    'booking':       ('Bookings & scheduling',    'Booking system',             'Calendar with availability and automatic confirmation'),
    'recurring':     ('Bookings & scheduling',    'Recurring payments / membership', 'Automatic monthly billing for subscribers'),
    'chatbot':       ('Automation & AI',          'AI chatbot',                 'Conversational assistant trained on your business information'),
    'smartform':     ('Automation & AI',          'Smart forms',                'Conditional logic, validation and delivery to CRM or email'),
    'notifications': ('Automation & AI',          'Automatic notifications',    'Automated emails and/or WhatsApp messages triggered by site events'),
    'analytics':     ('Analytics & SEO',          'Analytics dashboard',        'Visits, conversions and key business metrics'),
    'seo':           ('Analytics & SEO',          'Technical SEO',              'Meta tags, sitemap, Schema.org and page speed'),
    'reports':       ('Analytics & SEO',          'Monthly reports',            'Automated PDF report summarizing traffic and metrics'),
    'hosting':       ('Infrastructure',           'Managed hosting + domain',   'Server management, SSL and domain renewal'),
    'support':       ('Infrastructure',           'Support & maintenance',      'Bug fixes, updates and up to 3 hours of support per month'),
    'backup':        ('Infrastructure',           'Automatic backup',           'Daily backups with restoration within 24h'),
}

PACKS_EN = {
    'vitrina': 'Small business',
    'ecommerce': 'E-commerce',
    'restaurante': 'Restaurant',
    'clinica': 'Clinic / Medical',
    'gym': 'Gym / Sports',
    'inmobiliaria': 'Real estate',
}

# Textos de la interfaz que usa calculadora.js.
UI = {
    'es': {
        'mes': '/mes',
        'vacio': 'Ninguna feature seleccionada aún',
        'hint_vacio': 'Selecciona al menos una funcionalidad para solicitar tu presupuesto',
        'hint_ok': 'Respondo en menos de 24 horas',
        'enviando': 'Enviando...',
        'enviar': 'Enviar solicitud',
        'error_generico': 'No se pudo enviar la solicitud. Intenta nuevamente.',
        'error_red': 'No se pudo enviar la solicitud. Revisa tu conexión e intenta nuevamente.',
        'locale': 'es-CL',
    },
    'en': {
        'mes': '/mo',
        'vacio': 'No features selected yet',
        'hint_vacio': 'Select at least one feature to request your quote',
        'hint_ok': 'I reply within 24 hours',
        'enviando': 'Sending...',
        'enviar': 'Send request',
        'error_generico': 'The request could not be sent. Please try again.',
        'error_red': 'The request could not be sent. Check your connection and try again.',
        'locale': 'en-US',
    },
}


def catalogo(lang='es'):
    """Catálogo listo para el navegador, con textos en el idioma pedido."""
    if lang == 'en':
        features = [
            {**f, 'cat': FEATURES_EN[f['id']][0], 'name': FEATURES_EN[f['id']][1], 'desc': FEATURES_EN[f['id']][2]}
            for f in FEATURES
        ]
        packs = {k: {**v, 'label': PACKS_EN[k]} for k, v in PACKS.items()}
    else:
        features, packs = FEATURES, PACKS
    return {'features': features, 'packs': packs, 'implementacion': IMPLEMENTACION, 'ui': UI.get(lang, UI['es'])}


def calcular(ids):
    """Devuelve (funcionalidades, total_mensual, total_primer_anio) a partir de ids válidos.

    Ignora ids desconocidos y duplicados; el orden es el del catálogo.
    """
    elegidas = [f for f in FEATURES if f['id'] in set(ids)]
    mensual = sum(f['price'] for f in elegidas)
    return elegidas, mensual, IMPLEMENTACION + mensual * 12
