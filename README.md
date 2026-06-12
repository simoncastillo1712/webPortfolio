# Portafolio Web — Simón Castillo A.

Portafolio profesional en producción en [www.simoncastillo.cl](https://www.simoncastillo.cl), desarrollado con Django y Bootstrap 5.

---

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend | Python 3 · Django 6.0.3 |
| Frontend | Bootstrap 5.3.2 · CSS personalizado (glassmorphism) |
| Base de datos | PostgreSQL (producción) · SQLite (desarrollo local) |
| Email | Resend SDK (HTTP API) |
| Servidor | Gunicorn · WhiteNoise |
| Despliegue | Railway (nixpacks) |
| Dominio | HostGator DNS · Cloudflare |

---

## Características

- Diseño dark con efecto glassmorphism y gradientes radiales
- Sección de proyectos con links directos a repositorios GitHub
- Formulario de contacto: guarda mensajes en PostgreSQL y envía email vía Resend
- Actividad GitHub integrada con `github-readme-stats`
- Variables de entorno gestionadas con `python-decouple`
- Archivos estáticos servidos con WhiteNoise

---

## Estructura del proyecto

```
webPortafolio/
├── config/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── portafolio/
│       ├── templates/
│       │   ├── base.html
│       │   ├── inicio.html
│       │   ├── sobreMi.html
│       │   ├── proyectos.html
│       │   └── contacto.html
│       ├── static/img/
│       ├── models.py
│       ├── views.py
│       └── urls.py
├── requirements.txt
├── railway.toml
└── .env  (no incluido en el repo)
```

---

## Instalación local

```bash
# Clonar el repositorio
git clone https://github.com/simoncastillo1712/webPortfolio.git
cd webPortfolio

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo de variables de entorno
# (ver sección Variables de entorno)

# Migraciones y servidor
cd config
python manage.py migrate
python manage.py runserver
```

---

## Variables de entorno

Crear `config/.env` con:

```env
SECRET_KEY=tu-secret-key-aqui
DEBUG=True
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxx
EMAIL_FROM=contacto@tudominio.cl
CONTACT_EMAIL=tu@email.com
```

En producción (Railway) agregar también:
- `DATABASE_URL` — URL de conexión PostgreSQL
- `RAILWAY_ENVIRONMENT` — cualquier valor activa modo Railway (ALLOWED_HOSTS permisivo)

---

## Despliegue en Railway

El proyecto usa `railway.toml`:

```toml
[build]
builder = "nixpacks"
buildCommand = "cd config && python manage.py collectstatic --noinput"

[deploy]
startCommand = "cd config && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"
```

---

## Rutas disponibles

| Ruta | Vista |
|---|---|
| `/` | Inicio |
| `/sobre-mi/` | Sobre mí |
| `/proyectos/` | Proyectos |
| `/contacto/` | Contacto (formulario funcional) |
| `/admin/` | Panel de administración Django |

---

## Autor

**Simón Castillo A.** — Desarrollador Web · Diseñador · Científico de Datos

- Sitio: [www.simoncastillo.cl](https://www.simoncastillo.cl)
- Email: [contacto@simoncastillo.cl](mailto:contacto@simoncastillo.cl)
- LinkedIn: [linkedin.com/in/simón-castillo-armijo](https://www.linkedin.com/in/sim%C3%B3n-castillo-armijo)
- GitHub: [github.com/simoncastillo1712](https://github.com/simoncastillo1712)
