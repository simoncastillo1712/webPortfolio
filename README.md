# Portafolio Web Profesional — Simón Castillo A.

Sitio web de portafolio profesional desarrollado con **Django** y **Bootstrap**, orientado a mostrar experiencia, habilidades, proyectos tecnológicos y canales de contacto.

Este repositorio contiene una aplicación web con enfoque de presentación profesional, navegación clara por secciones y evidencias visuales de proyectos en desarrollo web y ciencia de datos.

---

## Tabla de contenidos

- [1. Descripción general](#1-descripción-general)
- [2. Objetivos del proyecto](#2-objetivos-del-proyecto)
- [3. Stack tecnológico](#3-stack-tecnológico)
- [4. Arquitectura y estructura del proyecto](#4-arquitectura-y-estructura-del-proyecto)
- [5. Requisitos previos](#5-requisitos-previos)
- [6. Instalación y ejecución local (paso a paso)](#6-instalación-y-ejecución-local-paso-a-paso)
- [7. Rutas y funcionalidades](#7-rutas-y-funcionalidades)
- [8. Gestión de archivos estáticos](#8-gestión-de-archivos-estáticos)
- [9. Personalización del contenido](#9-personalización-del-contenido)
- [10. Buenas prácticas para despliegue](#10-buenas-prácticas-para-despliegue)
- [11. Troubleshooting (solución de problemas)](#11-troubleshooting-solución-de-problemas)
- [12. Autor y contacto](#12-autor-y-contacto)

---

## 1. Descripción general

Este proyecto implementa un portafolio web personal/profesional con una estructura de vistas simples basada en Django:

- **Inicio**
- **Sobre mí**
- **Proyectos**
- **Contacto**

La aplicación está construida para entregar una experiencia visual moderna (tema oscuro, estilo glassmorphism y componentes Bootstrap), junto con contenido profesional orientado a empleabilidad y presentación de soluciones reales.

---

## 2. Objetivos del proyecto

- Centralizar la presentación del perfil profesional y técnico.
- Mostrar proyectos desarrollados con evidencia visual y contexto funcional.
- Facilitar el contacto laboral/profesional desde una página dedicada.
- Mantener una base de código clara y escalable para futuras mejoras (formularios, modelos, panel admin extendido, etc.).

---

## 3. Stack tecnológico

### Backend
- **Python**
- **Django 6.0.3**

### Frontend
- **HTML5** (templates Django)
- **CSS3** (estilos embebidos y clases personalizadas)
- **Bootstrap 5.3.2** (CDN)
- **JavaScript** (Bootstrap bundle vía CDN)

### Base de datos
- **SQLite3** (entorno local por defecto de Django)

### Gestión de assets
- Archivos estáticos gestionados mediante `static/` de la app `portafolio`.
- Recursos incluidos:
  - Imágenes de proyectos
  - PDF de CV
  - Notebook asociado a proyecto de minería (referencia de contenido técnico)

---

## 4. Arquitectura y estructura del proyecto

Estructura principal observada:

```text
webPortafolio/
├── README.md
└── config/
    ├── manage.py
    ├── db.sqlite3
    ├── config/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── portafolio/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── migrations/
        │   └── __init__.py
        ├── templates/
        │   ├── base.html
        │   ├── inicio.html
        │   ├── sobreMi.html
        │   ├── proyectos.html
        │   └── contacto.html
        └── static/
            ├── docs/
            │   └── CV Simon Castillo (Tech).pdf
            └── img/
                ├── adoptame/
                ├── billetera digital/
                ├── mineria/
                ├── supermercado/
                └── tickets/
```

### Explicación rápida por módulo

- `config/config/settings.py`: configuración general de Django (apps, base de datos, estáticos, etc.).
- `config/config/urls.py`: ruteo raíz, incluye rutas de `portafolio/` y redirección de `/` a `/portafolio/`.
- `config/portafolio/urls.py`: rutas específicas de la app.
- `config/portafolio/views.py`: funciones de vista que renderizan templates.
- `config/portafolio/templates/`: vistas HTML del sitio.
- `config/portafolio/static/`: imágenes, CV y otros recursos estáticos.

---

## 5. Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener:

- **Python 3.11+** (recomendado)
- **pip** actualizado
- Terminal en Windows / Linux / macOS

Verificación rápida:

```bash
python --version
pip --version
```

> En algunos entornos, puede ser necesario usar `py` en vez de `python`.

---

## 6. Instalación y ejecución local (paso a paso)

### 6.1 Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd webPortafolio
```

### 6.2 Crear y activar entorno virtual

#### Windows (CMD)
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 6.3 Instalar dependencias

Si cuentas con `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si no existe todavía, instalación mínima para este proyecto:

```bash
pip install django
```

### 6.4 Aplicar migraciones

```bash
cd config
python manage.py migrate
```

### 6.5 Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

### 6.6 Abrir en navegador

- URL principal del proyecto (redirección):  
  `http://127.0.0.1:8000/`
- URL directa del portafolio:  
  `http://127.0.0.1:8000/portafolio/`

---

## 7. Rutas y funcionalidades

Rutas actuales definidas:

### Rutas raíz del proyecto (`config/config/urls.py`)

- `/admin/` → panel administrativo de Django
- `/portafolio/` → incluye rutas de la app `portafolio`
- `/` → redirecciona a `/portafolio/`

### Rutas de la app `portafolio` (`config/portafolio/urls.py`)

- `/portafolio/` → `inicio`
- `/portafolio/sobre-mi` → `sobre_mi`
- `/portafolio/proyectos/` → `proyectos`
- `/portafolio/contacto/` → `contacto`
- `/portafolio/agregar-proyecto/` → `agregar_proyecto` *(actualmente renderiza proyectos.html)*
- `/portafolio/editar-proyecto/<int:proyecto_id>/` → `editar_proyecto` *(actualmente renderiza proyectos.html)*
- `/portafolio/eliminar-proyecto/<int:proyecto_id>/` → `eliminar_proyecto` *(actualmente renderiza proyectos.html)*

> Nota: Las tres rutas de agregar/editar/eliminar están como base funcional visual. No hay lógica CRUD persistente implementada aún en modelos/formularios.

---

## 8. Gestión de archivos estáticos

El proyecto usa la convención de Django con:

- `STATIC_URL = 'static/'`
- Archivos ubicados en `config/portafolio/static/`

### ¿Qué contiene actualmente?
- `docs/` para CV en PDF.
- `img/` con subcarpetas para capturas de distintos proyectos:
  - `adoptame`
  - `billetera digital`
  - `mineria`
  - `supermercado`
  - `tickets`

### Uso en templates
En templates se carga `{% load static %}` y se referencian assets con:

```django
{% static 'img/ruta/archivo.png' %}
```

---

## 9. Personalización del contenido

### 9.1 Editar textos y secciones

Archivos recomendados:

- `config/portafolio/templates/inicio.html`
- `config/portafolio/templates/sobreMi.html`
- `config/portafolio/templates/proyectos.html`
- `config/portafolio/templates/contacto.html`

### 9.2 Cambiar diseño base global

Modificar:

- `config/portafolio/templates/base.html`

Este archivo centraliza:
- navbar
- footer
- estilos globales (paleta, botones, tarjetas, hover, etc.)
- carga de Bootstrap

### 9.3 Modificar navegación y rutas

- Ajustar rutas en `config/portafolio/urls.py`
- Asegurar correspondencia con vistas en `config/portafolio/views.py`
- Si agregas nuevas páginas, enlázalas desde `base.html`

### 9.4 Actualizar enlaces externos

Revisar:
- GitHub
- LinkedIn
- YouTube
- correo y teléfono
- enlace de descarga de CV

Estos están mayormente en `proyectos.html` y `contacto.html`.

---

## 10. Buenas prácticas para despliegue

Antes de pasar a producción:

1. **Desactivar debug**
   ```python
   DEBUG = False
   ```

2. **Configurar hosts permitidos**
   ```python
   ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']
   ```

3. **Gestionar estáticos para producción**
   - Definir `STATIC_ROOT`
   - Ejecutar:
     ```bash
     python manage.py collectstatic
     ```

4. **Secret Key segura**
   - Nunca exponer la `SECRET_KEY` en repositorios públicos.
   - Mover secretos a variables de entorno (`.env` o panel del proveedor).

5. **Base de datos**
   - SQLite es suficiente para desarrollo.
   - En producción, evaluar PostgreSQL u otra alternativa robusta.

---

## 11. Troubleshooting (solución de problemas)

### Error: `No module named django`
Instala dependencias:
```bash
pip install django
```

### Error: `python` no reconocido
En Windows prueba:
```bash
py --version
py manage.py runserver
```

### No cargan imágenes o PDF
- Verifica `{% load static %}` en template.
- Verifica ruta exacta dentro de `static/`.
- Confirma nombre de archivos (incluyendo espacios y mayúsculas/minúsculas).

### Puerto ocupado (`runserver`)
Usa otro puerto:
```bash
python manage.py runserver 8001
```

### Cambios HTML no visibles
- Refrescar con `Ctrl + F5`.
- Reiniciar servidor de desarrollo.
- Revisar errores de sintaxis en template.

---

## 12. Autor y contacto

**Simón Adrián Castillo Armijo**  
Diseñador, Desarrollador Web y Científico de Datos (en formación)

- **Email:** simon.castillo.a@gmail.com  
- **Teléfono:** +56 9 5888 3107  
- **GitHub:** [github.com/simoncastillo1712](https://github.com/simoncastillo1712)  
- **LinkedIn:** [linkedin.com/in/simón-castillo-armijo](https://www.linkedin.com/in/simón-castillo-armijo)  
- **Ubicación:** Santiago de Chile

---

## Estado del proyecto

Proyecto funcional para presentación profesional, en evolución continua para incorporar mejoras de arquitectura, formularios, persistencia de datos y despliegue productivo.
