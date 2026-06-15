/* ============================================================
   calculadora.js
   Simón Castillo A. — Calculadora de Presupuesto Web
   ============================================================ */

const FEATURES = [
  // --- Contenido y administración ---
  { id: 'cms',        cat: 'Contenido y administración', name: 'Panel CMS',               desc: 'Editor visual para que el cliente actualice sin tocar código',  price: 18000 },
  { id: 'blog',       cat: 'Contenido y administración', name: 'Blog / noticias',          desc: 'Publicaciones con categorías, etiquetas y SEO básico',          price: 12000 },
  { id: 'gallery',    cat: 'Contenido y administración', name: 'Galería multimedia',        desc: 'Imágenes y videos optimizados con gestor de archivos',          price: 10000 },
  { id: 'multilang',  cat: 'Contenido y administración', name: 'Multi-idioma (i18n)',       desc: 'Versiones del sitio en más de un idioma con cambio dinámico',  price: 22000 },

  // --- E-commerce y pagos ---
  { id: 'cart',         cat: 'E-commerce y pagos', name: 'Carro de compras',        desc: 'Gestión de productos, stock y órdenes',                          price: 35000 },
  { id: 'payment',      cat: 'E-commerce y pagos', name: 'Pasarela de pago (API)',   desc: 'Integración con Transbank, MercadoPago, Stripe u otro',          price: 28000 },
  { id: 'clientportal', cat: 'E-commerce y pagos', name: 'Portal de clientes',       desc: 'Login, historial de compras y seguimiento de pedidos',           price: 22000 },
  { id: 'coupons',      cat: 'E-commerce y pagos', name: 'Cupones y descuentos',     desc: 'Códigos promocionales y precios dinámicos',                      price: 15000 },

  // --- Reservas y agenda ---
  { id: 'booking',   cat: 'Reservas y agenda', name: 'Sistema de reservas',         desc: 'Calendario con disponibilidad y confirmación automática',        price: 25000 },
  { id: 'recurring', cat: 'Reservas y agenda', name: 'Pago recurrente / membresía', desc: 'Cobro mensual automático a suscriptores',                        price: 28000 },

  // --- Automatización e IA ---
  { id: 'chatbot',       cat: 'Automatización e IA', name: 'Chatbot con IA',              desc: 'Asistente conversacional entrenado con info del negocio',      price: 45000 },
  { id: 'smartform',     cat: 'Automatización e IA', name: 'Formularios inteligentes',    desc: 'Lógica condicional, validación y envío a CRM o email',         price: 12000 },
  { id: 'notifications', cat: 'Automatización e IA', name: 'Notificaciones automáticas',  desc: 'Emails y/o WhatsApp automáticos por eventos del sitio',        price: 18000 },

  // --- Analytics y SEO ---
  { id: 'analytics', cat: 'Analytics y SEO', name: 'Dashboard de analytics', desc: 'Visitas, conversiones y métricas clave del negocio',             price: 15000 },
  { id: 'seo',       cat: 'Analytics y SEO', name: 'SEO técnico',            desc: 'Meta tags, sitemap, Schema.org y velocidad de carga',           price: 15000 },
  { id: 'reports',   cat: 'Analytics y SEO', name: 'Reportes mensuales',     desc: 'Informe PDF automático con resumen de tráfico y métricas',      price: 12000 },

  // --- Infraestructura ---
  { id: 'hosting', cat: 'Infraestructura', name: 'Hosting + dominio gestionado', desc: 'Gestión de servidor, SSL y renovación de dominio',             price: 20000 },
  { id: 'support', cat: 'Infraestructura', name: 'Soporte y mantención',         desc: 'Corrección de bugs, actualizaciones y soporte hasta 3h/mes',  price: 30000 },
  { id: 'backup',  cat: 'Infraestructura', name: 'Backup automático',            desc: 'Copias de seguridad diarias con restauración en 24h',         price: 12000 },
];

const PACKS = {
  vitrina:     { label: 'Comercio pequeño',   features: ['cms', 'smartform', 'seo', 'hosting', 'support'] },
  ecommerce:   { label: 'E-commerce',         features: ['cart', 'payment', 'clientportal', 'coupons', 'notifications', 'analytics', 'hosting', 'support', 'backup'] },
  restaurante: { label: 'Restaurante',         features: ['cms', 'booking', 'gallery', 'notifications', 'seo', 'hosting', 'support'] },
  clinica:     { label: 'Clínica / Médico',   features: ['booking', 'clientportal', 'chatbot', 'payment', 'notifications', 'blog', 'seo', 'hosting', 'support', 'backup'] },
  gym:         { label: 'Gym / Deportivo',     features: ['cart', 'payment', 'recurring', 'clientportal', 'notifications', 'gallery', 'cms', 'hosting', 'support'] },
  inmobiliaria:{ label: 'Inmobiliaria',        features: ['cms', 'chatbot', 'smartform', 'gallery', 'notifications', 'blog', 'seo', 'hosting', 'support', 'backup'] },
};

const selected = new Set();

/* ---------- helpers ---------- */
function fmt(n) {
  return '$' + n.toLocaleString('es-CL');
}

function packTotal(key) {
  return PACKS[key].features.reduce((sum, id) => {
    const f = FEATURES.find(x => x.id === id);
    return sum + (f ? f.price : 0);
  }, 0);
}

/* ---------- render features ---------- */
function renderFeatures() {
  const cats = [...new Set(FEATURES.map(f => f.cat))];
  const container = document.getElementById('features-container');

  container.innerHTML = cats.map(cat => {
    const rows = FEATURES.filter(f => f.cat === cat).map(f => {
      const active = selected.has(f.id);
      return `
        <div
          class="calc-feature-row ${active ? 'calc-feature-row--active' : ''}"
          onclick="toggle('${f.id}')"
          role="checkbox"
          aria-checked="${active}"
          tabindex="0"
          onkeydown="if(event.key==='Enter'||event.key===' ')toggle('${f.id}')"
        >
          <div class="calc-feature-row__left">
            <i class="bi ${active ? 'bi-check-circle-fill' : 'bi-circle'} calc-feature-row__icon ${active ? 'calc-feature-row__icon--active' : ''}"></i>
            <div>
              <p class="calc-feature-row__name">${f.name}</p>
              <p class="calc-feature-row__desc">${f.desc}</p>
            </div>
          </div>
          <span class="calc-feature-row__price">${fmt(f.price)}/mes</span>
        </div>`;
    }).join('');

    return `
      <p class="calc-cat-label">${cat}</p>
      ${rows}`;
  }).join('');
}

/* ---------- render pack buttons ---------- */
function renderPacks() {
  const container = document.getElementById('pack-buttons');
  container.innerHTML = Object.entries(PACKS).map(([key, pack]) => `
    <button class="calc-pack-btn" onclick="loadPack('${key}')">
      <span class="calc-pack-btn__name">${pack.label}</span>
      <span class="calc-pack-btn__price">${fmt(packTotal(key))}/mes</span>
    </button>
  `).join('');
}

/* ---------- update panel ---------- */
function updatePanel() {
  const items = FEATURES.filter(f => selected.has(f.id));
  const monthly = items.reduce((s, f) => s + f.price, 0);
  const year = 350000 + monthly * 12;

  document.getElementById('total-monthly').textContent = fmt(monthly);
  document.getElementById('total-year').textContent = fmt(year);
  document.getElementById('count').textContent = items.length;

  const list = document.getElementById('selected-list');
  list.innerHTML = items.length === 0
    ? '<li class="calc-empty-msg">Ninguna feature seleccionada aún</li>'
    : items.map(f => `
        <li class="calc-selected-item">
          <span>${f.name}</span>
          <span class="calc-selected-item__price">${fmt(f.price)}</span>
        </li>`).join('');
}

/* ---------- acciones ---------- */
function toggle(id) {
  selected.has(id) ? selected.delete(id) : selected.add(id);
  renderFeatures();
  updatePanel();
}

function clearAll() {
  selected.clear();
  renderFeatures();
  updatePanel();
}

function loadPack(key) {
  selected.clear();
  PACKS[key].features.forEach(id => selected.add(id));
  renderFeatures();
  updatePanel();
}

/* ---------- init ---------- */
document.addEventListener('DOMContentLoaded', () => {
  renderFeatures();
  renderPacks();
  updatePanel();
});
