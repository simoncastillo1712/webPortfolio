# Calculadora de Presupuesto Web
## Instrucciones de integración — simoncastillo.cl (Django)

---

## Archivos incluidos

```
calculadora_simon/
├── templates/
│   └── calculadora.html       # Template Django (extiende base.html)
├── static/
│   ├── css/
│   │   └── calculadora.css    # Estilos con paleta oscura de tu sitio
│   └── js/
│       └── calculadora.js     # Lógica de la calculadora
├── views.py                   # Vista a agregar en tu views.py
└── urls.py                    # URL a agregar en tu urls.py
```

---

## Pasos para integrar con Claude Code

### 1. Copiar los archivos estáticos

```bash
# Copia el CSS y JS a tu carpeta static existente
cp calculadora.css  tu_app/static/css/calculadora.css
cp calculadora.js   tu_app/static/js/calculadora.js
```

### 2. Copiar el template

```bash
cp calculadora.html  tu_app/templates/calculadora.html
```

> ⚠️ Verifica que `calculadora.html` use `{% extends "base.html" %}` con el mismo
> nombre de tu base template. Si tu base se llama diferente (p.ej. `layout.html`),
> cámbialo en la primera línea del template.

### 3. Agregar la vista en views.py

Abre tu `views.py` y añade al final:

```python
def calculadora(request):
    return render(request, 'calculadora.html')
```

### 4. Agregar la URL en urls.py

Abre tu `urls.py` y añade en `urlpatterns`:

```python
path('calculadora/', views.calculadora, name='calculadora'),
```

### 5. Agregar el link en la navbar

En tu `base.html` o donde tengas la navegación, añade:

```html
<li><a href="{% url 'calculadora' %}">Calculadora</a></li>
```

### 6. Verificar Bootstrap Icons

Tu sitio ya usa Bootstrap 5. Confirma que en tu `base.html` tengas cargado
Bootstrap Icons (para los íconos bi-circle, bi-check-circle-fill):

```html
<link rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
```

Si ya lo tienes, no hace falta agregarlo de nuevo.

### 7. Collectstatic (producción)

```bash
python manage.py collectstatic
```

### 8. Probar en local

```bash
python manage.py runserver
# Visita: http://127.0.0.1:8000/calculadora/
```

---

## Personalización rápida

### Cambiar precios
Edita el array `FEATURES` en `calculadora.js`. Cada feature tiene:
```js
{ id: 'cms', cat: 'Categoría', name: 'Nombre', desc: 'Descripción', price: 18000 }
```

### Agregar un pack nuevo
Edita el objeto `PACKS` en `calculadora.js`:
```js
salon: { label: 'Salón / Spa', features: ['booking', 'gallery', 'notifications', 'seo', 'hosting', 'support'] },
```

### Cambiar el CTA
En `calculadora.html`, el botón "Solicitar presupuesto" apunta a `{% url 'contacto' %}`.
Si tu URL de contacto tiene otro nombre, cámbialo ahí.

---

## Prompt sugerido para Claude Code

Pega esto en Claude Code para que haga la integración automáticamente:

```
Tengo un proyecto Django en [ruta de tu proyecto].
Quiero integrar una calculadora de presupuesto web.
Los archivos están en la carpeta calculadora_simon/:
- templates/calculadora.html → copiar a [tu_app]/templates/
- static/css/calculadora.css → copiar a [tu_app]/static/css/
- static/js/calculadora.js  → copiar a [tu_app]/static/js/
- Añadir la vista de views.py a [tu_app]/views.py
- Añadir la URL de urls.py a [tu_app]/urls.py
- Añadir un link "Calculadora" en la navbar de base.html
- Verificar que Bootstrap Icons esté cargado en base.html
Por favor realiza todos estos cambios manteniendo el estilo existente del sitio.
```
