/* ============================================================
   calculadora.js
   Simón Castillo A. — Calculadora de Presupuesto Web
   ============================================================ */

/* El catálogo (funcionalidades, packs e implementación) viene del servidor:
   ver presupuesto.py. El servidor además recalcula los precios al recibir la solicitud. */
const CATALOGO = JSON.parse(document.getElementById('catalogo-data').textContent);
const FEATURES = CATALOGO.features;
const PACKS = CATALOGO.packs;
const IMPLEMENTACION = CATALOGO.implementacion;
const UI = CATALOGO.ui;  // textos de la interfaz en el idioma de la página

const selected = new Set();

/* ---------- helpers ---------- */
function fmt(n) {
  return '$' + n.toLocaleString(UI.locale);
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
          <span class="calc-feature-row__price">${fmt(f.price)}${UI.mes}</span>
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
      <span class="calc-pack-btn__price">${fmt(packTotal(key))}${UI.mes}</span>
    </button>
  `).join('');
}

/* ---------- update panel ---------- */
function updatePanel() {
  const items = FEATURES.filter(f => selected.has(f.id));
  const monthly = items.reduce((s, f) => s + f.price, 0);
  const year = IMPLEMENTACION + monthly * 12;

  document.getElementById('total-monthly').textContent = fmt(monthly);
  document.getElementById('total-year').textContent = fmt(year);
  document.getElementById('count').textContent = items.length;

  const list = document.getElementById('selected-list');
  list.innerHTML = items.length === 0
    ? `<li class="calc-empty-msg">${UI.vacio}</li>`
    : items.map(f => `
        <li class="calc-selected-item">
          <span>${f.name}</span>
          <span class="calc-selected-item__price">${fmt(f.price)}</span>
        </li>`).join('');

  const btn = document.getElementById('btn-solicitar');
  if (btn) btn.disabled = items.length === 0;
  const hint = document.getElementById('cta-hint');
  if (hint) hint.textContent = items.length === 0
    ? UI.hint_vacio
    : UI.hint_ok;
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

/* ---------- modal de solicitud ---------- */
function renderModalSummary() {
  const items = FEATURES.filter(f => selected.has(f.id));
  const monthly = items.reduce((s, f) => s + f.price, 0);
  document.getElementById('modal-count').textContent = items.length;
  document.getElementById('modal-list').innerHTML = items.map(f => `
    <li class="calc-selected-item">
      <span>${f.name}</span>
      <span class="calc-selected-item__price">${fmt(f.price)}${UI.mes}</span>
    </li>`).join('');
  document.getElementById('modal-impl').textContent = fmt(IMPLEMENTACION);
  document.getElementById('modal-monthly').textContent = fmt(monthly);
  document.getElementById('modal-year').textContent = fmt(IMPLEMENTACION + monthly * 12);
}

function initModal() {
  const modalEl = document.getElementById('modalPresupuesto');
  const form = document.getElementById('form-presupuesto');
  const errorBox = document.getElementById('modal-error');
  const sendBtn = document.getElementById('pp-enviar');

  modalEl.addEventListener('show.bs.modal', () => {
    renderModalSummary();
    errorBox.hidden = true;
    document.getElementById('modal-exito').hidden = true;
    document.getElementById('modal-formulario').hidden = false;
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorBox.hidden = true;
    const data = new FormData(form);
    selected.forEach(id => data.append('features', id));

    sendBtn.disabled = true;
    sendBtn.textContent = UI.enviando;
    try {
      const res = await fetch(form.action, {
        method: 'POST',
        body: data,
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
      });
      const json = await res.json().catch(() => ({}));
      if (res.ok && json.ok) {
        form.reset();
        document.getElementById('modal-formulario').hidden = true;
        document.getElementById('modal-exito').hidden = false;
      } else {
        errorBox.textContent = json.error || UI.error_generico;
        errorBox.hidden = false;
      }
    } catch (err) {
      errorBox.textContent = UI.error_red;
      errorBox.hidden = false;
    } finally {
      sendBtn.disabled = false;
      sendBtn.textContent = UI.enviar;
    }
  });
}

/* ---------- init ---------- */
document.addEventListener('DOMContentLoaded', () => {
  renderFeatures();
  renderPacks();
  updatePanel();
  initModal();
});
