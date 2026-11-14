// Behaviour of the start page: language menu, feature slider, live spots,
// live numbers and the search box. No cookies, no storage, no tracking.

const SPOTS = 'https://spots.wwff.co/static/spots.json';
const AGENDA_ACTIVE = 'https://spots.wwff.co/static/agendas_active.json';
const AGENDA_ALL = 'https://spots.wwff.co/static/agendas.json';
const APP_DATA = 'https://diana-onff.github.io/data/';

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

function langMenu() {
  const sel = document.querySelector('[data-lang-select]');
  if (sel) sel.addEventListener('change', () => { window.location.href = sel.value; });
}

function slider() {
  const root = document.querySelector('[data-slider]');
  if (!root) return;
  const slides = [...root.querySelectorAll('[data-slide]')];
  const dots = [...root.querySelectorAll('[data-dot]')];
  const name = root.querySelector('[data-slide-name]');
  let i = 0;
  const show = (n) => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => { s.hidden = k !== i; });
    dots.forEach((d, k) => d.setAttribute('aria-selected', k === i ? 'true' : 'false'));
    if (name) name.textContent = dots[i]?.getAttribute('aria-label') ?? '';
  };
  root.querySelector('[data-prev]')?.addEventListener('click', () => show(i - 1));
  root.querySelector('[data-next]')?.addEventListener('click', () => show(i + 1));
  dots.forEach((d, k) => d.addEventListener('click', () => show(k)));
  const track = root.querySelector('[data-track]');
  let x0 = null;
  track?.addEventListener('touchstart', (e) => { x0 = e.changedTouches[0]?.clientX ?? null; }, { passive: true });
  track?.addEventListener('touchend', (e) => {
    const x = e.changedTouches[0]?.clientX;
    if (x0 == null || x == null) return;
    const dx = x - x0; x0 = null;
    if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1));
  });
  root.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') show(i - 1);
    if (e.key === 'ArrowRight') show(i + 1);
  });
}

async function liveSpots() {
  const box = document.querySelector('[data-live]');
  if (!box) return;
  const T = JSON.parse(box.dataset.t);
  const rowsEl = box.querySelector('[data-live-rows]');
  const set = (mode) => {
    const [label, title, link, note, cols] = T[mode];
    box.querySelector('[data-live-label]').textContent = label;
    box.querySelector('[data-live-title]').textContent = title;
    box.querySelector('[data-live-link]').textContent = link;
    box.querySelector('[data-live-note]').textContent = note;
    box.querySelectorAll('[data-live-col]').forEach((c, k) => { c.textContent = cols[k]; });
    box.querySelector('[data-live-dot]').classList.toggle('off', mode === 'off');
  };
  const ago = (sec) => {
    const m = Math.max(0, Math.round((Date.now() / 1000 - sec) / 60));
    return m < 60 ? T.min.replace('{n}', m) : T.h.replace('{n}', Math.round(m / 60));
  };
  const row = (a, b, c, d, e) => `<div class="live-row" role="row"><span role="cell" class="call">${esc(a)}</span><span role="cell"><span class="ref">${esc(b)}</span></span><span role="cell" class="mono">${esc(c)}</span><span role="cell">${esc(d)}</span><span role="cell" class="when">${esc(e)}</span></div>`;

  let shown = false;
  const show = () => { box.hidden = false; shown = true; };
  async function load() {
    try {
      const spots = await fetch(SPOTS, { cache: 'no-store' }).then((r) => r.json());
      const fresh = (Array.isArray(spots) ? spots : [])
        .filter((s) => Date.now() / 1000 - (s.spot_time || 0) < 30 * 60)
        .sort((a, b) => (b.spot_time || 0) - (a.spot_time || 0))
        .slice(0, 6);
      if (fresh.length) {
        set('on');
        rowsEl.innerHTML = fresh.map((s) => row(s.activator || '?', s.reference || '', `${s.frequency_khz || '?'} kHz`, s.mode || '', ago(s.spot_time || 0))).join('');
        show();
        return;
      }
      const [act, all] = await Promise.all([
        fetch(AGENDA_ACTIVE, { cache: 'no-store' }).then((r) => r.json()).catch(() => []),
        fetch(AGENDA_ALL, { cache: 'no-store' }).then((r) => r.json()).catch(() => []),
      ]);
      const now = new Date().toISOString().slice(0, 19).replace('T', ' ');
      const list = [...(Array.isArray(act) ? act : []), ...(Array.isArray(all) ? all : [])]
        .filter((a, k, arr) => arr.findIndex((b) => String(b.id) === String(a.id)) === k)
        .filter((a) => String(a.utc_end || a.utc_start || '') >= now)
        .sort((a, b) => String(a.utc_start).localeCompare(String(b.utc_start)))
        .slice(0, 6);
      if (!list.length) { if (!shown) box.hidden = true; return; }
      set('off');
      rowsEl.innerHTML = list.map((a) => row(a.activator_call || '?', a.reference || '', a.band || '', a.mode || '', `${String(a.utc_start || '').slice(5, 10)} ${String(a.utc_start || '').slice(11, 16)} UTC`)).join('');
      show();
    } catch {
      // Spotline not reachable: keep the last list if there is one, otherwise stay hidden.
      if (!shown) box.hidden = true;
    }
  }
  await load();
  setInterval(() => { if (!document.hidden) load(); }, 60000);
}

async function liveNumbers() {
  const lang = document.documentElement.lang || 'en';
  const fmt = (n) => new Intl.NumberFormat(lang).format(n);
  const put = (k, v) => { const el = document.querySelector(`[data-stat="${k}"]`); if (el && Number.isFinite(v)) el.textContent = fmt(v); };
  try {
    const [meta, countries, progs] = await Promise.all([
      fetch(`${APP_DATA}meta.json`).then((r) => r.json()),
      fetch(`${APP_DATA}countries.json`).then((r) => r.json()),
      fetch(`${APP_DATA}wwff-programs.json`).then((r) => r.json()),
    ]);
    put('refs', meta.world_points);
    put('countries', (countries.countries || []).length);
    const p = progs.programs;
    put('progs', Array.isArray(p) ? p.length : Object.keys(p || {}).length);
  } catch { /* keep the numbers printed in the page */ }
}

function search() {
  const form = document.querySelector('[data-search]');
  if (!form) return;
  const input = form.querySelector('input');
  const out = document.querySelector('[data-results]');
  let pf = null;
  let timer = null;
  const base = (document.querySelector('link[rel="icon"]')?.getAttribute('href') || '/icon-192.png').replace(/icon-192\.png$/, '');
  async function run() {
    const q = input.value.trim();
    if (q.length < 2) { out.hidden = true; out.innerHTML = ''; return; }
    try {
      if (!pf) {
        const url = `${base}pagefind/pagefind.js`;
        pf = await import(/* @vite-ignore */ url);
        await pf.init();
      }
      const res = await pf.search(q);
      const top = await Promise.all((res?.results || []).slice(0, 6).map((r) => r.data()));
      out.innerHTML = top.length
        ? top.map((d) => `<li><a href="${esc(d.url)}"><b>${esc(d.meta?.title || d.url)}</b><span>${d.excerpt}</span></a></li>`).join('')
        : `<li class="none">${esc(form.dataset.none)}</li>`;
      out.hidden = false;
    } catch {
      out.innerHTML = `<li class="none">${esc(form.dataset.none)}</li>`;
      out.hidden = false;
    }
  }
  input.addEventListener('input', () => { clearTimeout(timer); timer = setTimeout(run, 200); });
}

export function initLanding() {
  langMenu();
  slider();
  liveSpots();
  liveNumbers();
  search();
}
