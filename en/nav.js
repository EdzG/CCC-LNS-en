/* Study navigation for the CCC-LNS lecture pages: section scroll-spy, prev/next section and
 * chapter, a link to the study dashboard, per-chapter scroll restore, and quiz progress.
 * Loaded by one injected line per chapter (en/tools/inject.py --nav):
 *   <script src="../../en/nav.js" data-chapter="IDL_115/ChNN-xxx" defer></script>
 * Independent of toggle.js: it never calls it. It reads the page DOM, writes localStorage
 * keys under 'ccc-lns-study:', and marks its own UI data-en-skip so toggle.js ignores it.
 * See CLAUDE.md ("Study layer").
 */
(function () {
  'use strict';

  var script = document.currentScript || document.querySelector('script[src*="en/nav.js"]');
  var CHAPTER = script && script.getAttribute('data-chapter');
  if (!CHAPTER) return;
  var CH_ID = CHAPTER.split('/').pop();
  var ROOT = new URL('../', script.src).href;              // repo root
  var DASH = ROOT + 'study/index.html';
  var NS = 'ccc-lns-study:';
  // Quiz containers of the four page families. Must match QUIZ_CLASSES in study/build_chapters.py.
  var QUIZ_SEL = '.quiz, .quiz-container, .quiz-sec';
  var LINE = 0.25;                                          // reading line, as a fraction of the viewport

  // ---------- storage ----------
  function load(k) { try { return JSON.parse(localStorage.getItem(NS + k)); } catch (e) { return null; } }
  function save(k, v) { try { localStorage.setItem(NS + k, JSON.stringify(v)); } catch (e) { /* storage blocked */ } }

  // ---------- sections and quizzes ----------
  var cards = Array.prototype.filter.call(document.querySelectorAll('section.card[data-kp]'),
    function (c) { return /^kp\d+$/.test(c.id); });
  if (!cards.length) return;
  function badgeOf(c) { var b = c.querySelector('.badge, .card-badge'); return b ? b.textContent.trim() : String(c.dataset.kp); }
  function titleEl(c) { return c.querySelector('.card-title, .card-head h3'); }
  function quizzesOf(c) {
    return Array.prototype.filter.call(c.querySelectorAll(QUIZ_SEL),
      function (q) { return !q.parentElement.closest(QUIZ_SEL); });
  }

  var quiz = load('quiz:' + CH_ID) || { q: {} };
  function sectionDone(c) {
    var qs = quizzesOf(c);
    return qs.length > 0 && qs.every(function (q, i) { return quiz.q[c.id + '.' + i] === 1; });
  }

  // Runs after the page's own quiz handler (on the button, or registered earlier on document),
  // then reads the result from the classes the page set.
  document.addEventListener('click', function (e) {
    var q = e.target.closest && e.target.closest(QUIZ_SEL);
    if (!q || q.closest('[data-en-skip]')) return;
    var opt = e.target.closest('.quiz-option-btn');
    var check = e.target.closest('.check, .quiz-check');
    if (!opt && !check) return;
    if (check && !q.querySelector('input:checked')) return;     // "please choose first"
    setTimeout(function () {
      var c = q.closest('section.card[data-kp]');
      var i = c ? quizzesOf(c).indexOf(q) : -1;
      if (i < 0) return;
      var ok = !!(q.querySelector('.fb.ok, .quiz-feedback.ok, .quiz-feedback.correct') ||
                  (opt && opt.classList.contains('correct')));
      var k = c.id + '.' + i;
      if (quiz.q[k] !== 1) quiz.q[k] = ok ? 1 : 0;
      quiz.t = Date.now();
      save('quiz:' + CH_ID, quiz);
      markToc();
    }, 0);
  });

  // ---------- the page's own TOC (reused, never rebuilt) ----------
  var tocLinks = {};                                        // 'kp3' -> [a, ...]
  Array.prototype.forEach.call(document.querySelectorAll('a[href^="#kp"]'), function (a) {
    var id = a.getAttribute('href').slice(1);
    if (!/^kp\d+$/.test(id) || a.closest('section.card')) return;
    (tocLinks[id] = tocLinks[id] || []).push(a);
  });
  var allLinks = [].concat.apply([], Object.keys(tocLinks).map(function (k) { return tocLinks[k]; }));
  // Ch10/14/19 only have "KP 1 … KP n" links; those still get highlighted, but the
  // section list in the drawer is what shows titles there.
  var titledToc = allLinks.filter(function (a) { return !/^\s*(KP|§)?\s*[\d.]+\s*$/i.test(a.textContent); });
  var tocBox = titledToc.length ? titledToc[0].closest('nav, .toc') : null;

  function markToc() {
    cards.forEach(function (c) {
      var done = sectionDone(c);
      (tocLinks[c.id] || []).forEach(function (a) { a.classList.toggle('study-done', done); });
    });
    if (drawer && drawer.classList.contains('open')) fillDrawer();
  }

  // ---------- reading position ----------
  function line() { return window.innerHeight * LINE; }
  function currentIndex() {
    var y = line(), idx = -1;
    for (var i = 0; i < cards.length; i++) {
      if (cards[i].getBoundingClientRect().top <= y) idx = i; else break;
    }
    return idx;
  }
  function position() {
    var i = Math.max(0, currentIndex()), r = cards[i].getBoundingClientRect();
    var f = r.height ? (line() - r.top) / r.height : 0;
    return { kp: cards[i].id, f: Math.min(1, Math.max(0, f)), t: Date.now() };
  }
  function scrollToPos(p) {
    var c = document.getElementById(p.kp);
    if (!c) return false;
    var r = c.getBoundingClientRect();
    window.scrollTo({ top: r.top + window.scrollY + p.f * r.height - line(), behavior: 'instant' });
    return true;
  }

  var lastPos = null;
  function persist() {
    if (restoring) return;
    lastPos = position();
    save('pos:' + CH_ID, lastPos);
    var c = document.getElementById(lastPos.kp);
    save('last', { ch: CH_ID, kp: lastPos.kp, badge: badgeOf(c), t: lastPos.t });
  }

  // Restore: honor a #hash from a link, but not on a reload (then the hash is just the last
  // TOC click). Re-applied while KaTeX renders and toggle.js switches language, until the
  // reader scrolls or touches anything.
  var nav = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
  var saved = load('pos:' + CH_ID);
  var hashKp = /^#kp\d+$/.test(location.hash) && document.getElementById(location.hash.slice(1));
  var restoring = !!(saved && (!hashKp || (nav && nav.type === 'reload')));
  function reapply() { if (restoring && !scrollToPos(saved)) restoring = false; }
  function stopRestore() {
    if (!restoring) return;
    restoring = false;
    persist();
  }
  if (restoring) {
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
    ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) {
      window.addEventListener(ev, stopRestore, { passive: true, capture: true });
    });
    reapply();
    window.addEventListener('load', function () {
      [0, 120, 400, 900, 1700].forEach(function (ms) { setTimeout(reapply, ms); });
      setTimeout(stopRestore, 2500);
    });
  }

  // Language switches change text length; keep the reader on the same spot.
  new MutationObserver(function (recs) {
    var html = document.documentElement;
    var changed = recs.some(function (r) {
      return r.attributeName === 'lang' ? r.oldValue !== html.lang
        : /\ben-pending\b/.test(r.oldValue || '') && !html.classList.contains('en-pending');
    });
    var p = restoring ? saved : lastPos;
    if (!changed || !p) return;
    [0, 300].forEach(function (ms) { setTimeout(function () { scrollToPos(p); }, ms); });
  }).observe(document.documentElement, { attributes: true, attributeOldValue: true, attributeFilter: ['lang', 'class'] });

  // ---------- UI ----------
  var CSS = [
    ':root{--sn-bg:#ffffff;--sn-fg:#1f2430;--sn-muted:#64748b;--sn-border:#cbd5e1;--sn-hover:#f1f5f9;--sn-accent:#0d9488;--sn-on:#ffffff;--sn-done:#16a34a;--sn-shadow:0 4px 16px rgba(0,0,0,.16);}',
    '@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--sn-bg:#1e293b;--sn-fg:#e2e8f0;--sn-muted:#94a3b8;--sn-border:#475569;--sn-hover:#334155;--sn-accent:#14b8a6;--sn-on:#0f172a;--sn-done:#4ade80;--sn-shadow:0 4px 16px rgba(0,0,0,.5);}}',
    ':root[data-theme="dark"]{--sn-bg:#1e293b;--sn-fg:#e2e8f0;--sn-muted:#94a3b8;--sn-border:#475569;--sn-hover:#334155;--sn-accent:#14b8a6;--sn-on:#0f172a;--sn-done:#4ade80;--sn-shadow:0 4px 16px rgba(0,0,0,.5);}',
    '#study-nav{position:fixed;right:12px;bottom:12px;z-index:150;display:flex;align-items:center;gap:2px;padding:3px;border-radius:99px;border:1px solid var(--sn-border);background:var(--sn-bg);box-shadow:var(--sn-shadow);font:600 13px/1 system-ui,-apple-system,"Segoe UI",sans-serif;}',
    '#study-nav .sn-b{display:inline-flex;align-items:center;justify-content:center;min-width:34px;height:34px;padding:0 9px;border:0;border-radius:99px;background:none;color:var(--sn-fg);font:inherit;text-decoration:none;cursor:pointer;}',
    '#study-nav .sn-b:hover{background:var(--sn-hover);}',
    '#study-nav .sn-b[aria-disabled="true"]{color:var(--sn-muted);opacity:.45;pointer-events:none;}',
    '#study-nav .sn-pos{min-width:76px;font-variant-numeric:tabular-nums;}',
    '#study-nav .sn-sep{width:1px;height:20px;background:var(--sn-border);margin:0 2px;}',
    '#study-nav :focus-visible,#study-drawer :focus-visible{outline:2px solid var(--sn-accent);outline-offset:1px;}',
    '#study-drawer{position:fixed;right:12px;bottom:58px;z-index:150;width:min(340px,calc(100vw - 24px));max-height:min(70vh,560px);overflow:auto;display:none;padding:6px;border-radius:14px;border:1px solid var(--sn-border);background:var(--sn-bg);color:var(--sn-fg);box-shadow:var(--sn-shadow);font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;}',
    '#study-drawer.open{display:block;}',
    '#study-drawer .sn-h{padding:8px 10px 6px;color:var(--sn-muted);font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;}',
    '#study-drawer a{display:flex;gap:8px;align-items:baseline;padding:7px 10px;border-radius:8px;color:inherit;text-decoration:none;}',
    '#study-drawer a:hover{background:var(--sn-hover);}',
    '#study-drawer a.cur{background:var(--sn-accent);color:var(--sn-on);}',
    '#study-drawer .sn-badge{flex:none;min-width:2.6em;font-size:12px;font-weight:700;opacity:.8;font-variant-numeric:tabular-nums;}',
    '#study-drawer .sn-t{flex:1;min-width:0;}',
    '#study-drawer .sn-ok{flex:none;color:var(--sn-done);font-weight:700;}',
    '#study-drawer a.cur .sn-ok{color:inherit;}',
    '.study-active{box-shadow:inset 3px 0 0 var(--sn-accent);font-weight:600;}',
    '@keyframes study-flash{0%,60%{background:var(--sn-accent);color:var(--sn-on);}100%{}}',
    '.study-flash{animation:study-flash 1.2s ease-out;}',
    '.study-done::after{content:" \\2713";color:var(--sn-done);font-weight:700;}'
  ].join('\n');

  var bar, drawer, posBtn, prevB, nextB, prevCh, nextCh;
  function el(tag, attrs, text) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text) e.textContent = text;
    return e;
  }
  function buildUi() {
    var st = el('style', { id: 'study-nav-style' }); st.textContent = CSS;
    document.head.appendChild(st);
    bar = el('div', { id: 'study-nav', role: 'navigation', 'data-en-skip': '', 'aria-label': 'Study navigation' });   // not <nav>: pages style bare nav
    var home = el('a', { 'class': 'sn-b', href: DASH, title: 'Study dashboard', 'aria-label': 'Study dashboard' }, '⌂');
    prevCh = el('a', { 'class': 'sn-b', title: 'Previous chapter', 'aria-label': 'Previous chapter', 'aria-disabled': 'true' }, '«');
    prevB = el('button', { 'class': 'sn-b', type: 'button', title: 'Previous section', 'aria-label': 'Previous section' }, '‹');
    posBtn = el('button', { 'class': 'sn-b sn-pos', type: 'button', title: 'Sections', 'aria-haspopup': 'true', 'aria-expanded': 'false' });
    nextB = el('button', { 'class': 'sn-b', type: 'button', title: 'Next section', 'aria-label': 'Next section' }, '›');
    nextCh = el('a', { 'class': 'sn-b', title: 'Next chapter', 'aria-label': 'Next chapter', 'aria-disabled': 'true' }, '»');
    [home, el('span', { 'class': 'sn-sep' }), prevCh, prevB, posBtn, nextB, nextCh].forEach(function (n) { bar.appendChild(n); });
    drawer = el('div', { id: 'study-drawer', 'data-en-skip': '', role: 'dialog', 'aria-label': 'Sections' });
    document.body.appendChild(drawer);
    document.body.appendChild(bar);

    prevB.addEventListener('click', function () { go(Math.max(0, currentIndex() - 1)); });
    nextB.addEventListener('click', function () { go(Math.min(cards.length - 1, currentIndex() + 1)); });
    posBtn.addEventListener('click', function () {
      // The page's TOC is pinned on screen (desktop): point at it instead of duplicating it.
      if (tocPinned() && !drawer.classList.contains('open')) {
        var a = (tocLinks[cards[Math.max(0, currentIndex())].id] || []).filter(function (x) { return tocBox.contains(x); })[0];
        if (a) {
          keepInBox(a);
          a.classList.remove('study-flash'); void a.offsetWidth; a.classList.add('study-flash');
          return;
        }
      }
      toggleDrawer();
    });
    drawer.addEventListener('click', function (e) {
      var a = e.target.closest('a[data-i]');
      if (!a) return;
      e.preventDefault();
      toggleDrawer(false);
      go(+a.getAttribute('data-i'));
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggleDrawer(false); });
    document.addEventListener('click', function (e) {
      if (drawer.classList.contains('open') && !drawer.contains(e.target) && !bar.contains(e.target)) toggleDrawer(false);
    });
  }
  // Some pages are wider than a phone screen (demo canvases), so the layout viewport that
  // position:fixed uses is wider than what is visible. Pin the bar to the visual viewport.
  function fitViewport() {
    var vv = window.visualViewport;
    if (!vv) return;
    bar.style.transform = drawer.style.transform = '';
    var r = bar.getBoundingClientRect();
    var dx = Math.round(Math.min(0, vv.offsetLeft + vv.width - 12 - r.right));
    var dy = Math.round(Math.min(0, vv.offsetTop + vv.height - 12 - r.bottom));
    var t = dx || dy ? 'translate(' + dx + 'px,' + dy + 'px)' : '';
    bar.style.transform = drawer.style.transform = t;
  }
  function tocPinned() {
    if (!tocBox || !tocBox.getClientRects().length) return false;
    var r = tocBox.getBoundingClientRect();
    return /sticky|fixed/.test(getComputedStyle(tocBox).position) && r.width < window.innerWidth / 2 &&   // a sidebar, not a phone-width block
      r.bottom > 0 && r.top < window.innerHeight;
  }
  function keepInBox(a) {
    var box = a.closest('nav, .toc');
    if (!box || box.scrollHeight <= box.clientHeight) return;
    var r = a.getBoundingClientRect(), b = box.getBoundingClientRect();
    if (r.top < b.top + 8) box.scrollTop -= b.top + 8 - r.top;
    else if (r.bottom > b.bottom - 8) box.scrollTop += r.bottom - b.bottom + 8;
  }
  function go(i) {
    stopRestore();
    cards[i].scrollIntoView({ behavior: 'smooth', block: 'start' });   // respects the page's scroll-margin-top
  }
  function toggleDrawer(force) {
    var open = force === undefined ? !drawer.classList.contains('open') : force;
    if (open) fillDrawer();
    drawer.classList.toggle('open', open);
    posBtn.setAttribute('aria-expanded', String(open));
    if (open) { var cur = drawer.querySelector('a.cur'); if (cur) cur.scrollIntoView({ block: 'nearest' }); }
  }
  // Titles are copied from the live headings each time, so they follow the page language.
  function fillDrawer() {
    var cur = Math.max(0, currentIndex());
    drawer.textContent = '';
    drawer.appendChild(el('div', { 'class': 'sn-h' }, 'Sections'));
    cards.forEach(function (c, i) {
      var a = el('a', { href: '#' + c.id, 'data-i': String(i) });
      if (i === cur) { a.className = 'cur'; a.setAttribute('aria-current', 'true'); }
      a.appendChild(el('span', { 'class': 'sn-badge' }, badgeOf(c)));
      var t = el('span', { 'class': 'sn-t' }), h = titleEl(c);
      if (h) { t.innerHTML = h.innerHTML; t.querySelectorAll('[id]').forEach(function (n) { n.removeAttribute('id'); }); }
      a.appendChild(t);
      if (sectionDone(c)) a.appendChild(el('span', { 'class': 'sn-ok', 'aria-label': 'all quizzes solved' }, '✓'));
      drawer.appendChild(a);
    });
  }

  var shown = null;
  function update() {
    if (!restoring) lastPos = position();
    var i = currentIndex(), id = i < 0 ? null : cards[i].id;
    if (id !== shown) {
      if (shown) (tocLinks[shown] || []).forEach(function (a) { a.classList.remove('study-active'); a.removeAttribute('aria-current'); });
      if (id) (tocLinks[id] || []).forEach(function (a) { a.classList.add('study-active'); a.setAttribute('aria-current', 'location'); keepInBox(a); });
      shown = id;
    }
    var j = Math.max(0, i);                                   // above section 1 counts as section 1
    var badge = badgeOf(cards[j]).replace(/^§\s*/, '').split(/\s*[–-]\s*/)[0];   // '2.1.1–2.1.3' -> '2.1.1'
    posBtn.textContent = '§' + badge + ' · ' + (j + 1) + '/' + cards.length;
    posBtn.setAttribute('aria-label', 'Section ' + (j + 1) + ' of ' + cards.length + '. Show sections');
    prevB.disabled = i <= 0; prevB.setAttribute('aria-disabled', String(i <= 0));
    var last = i >= cards.length - 1;
    nextB.disabled = last; nextB.setAttribute('aria-disabled', String(last));
  }

  var ticking = false, saveTimer = null;
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; update(); }); }
    clearTimeout(saveTimer);
    saveTimer = setTimeout(persist, 400);
  }, { passive: true });
  window.addEventListener('pagehide', persist);
  document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') persist(); });

  // Prev/next chapter from the dashboard's chapter list.
  var chaptersReady = fetch(ROOT + 'study/chapters.json', { cache: 'no-cache' }).then(function (r) {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  }).then(function (d) {
    var list = d.chapters || [], i = list.map(function (c) { return c.id; }).indexOf(CH_ID);
    if (i < 0) return;
    [[prevCh, list[i - 1], 'Previous chapter'], [nextCh, list[i + 1], 'Next chapter']].forEach(function (x) {
      if (!x[1]) return;
      x[0].href = ROOT + x[1].lecture;
      x[0].removeAttribute('aria-disabled');
      x[0].title = x[2] + ': Ch' + String(x[1].num).padStart(2, '0') + ' ' + x[1].title;
    });
  }).catch(function () { /* no chapters.json: chapter buttons stay disabled */ });

  buildUi();
  fitViewport();
  if (window.visualViewport) {
    visualViewport.addEventListener('resize', fitViewport);
    visualViewport.addEventListener('scroll', fitViewport);
  }
  window.addEventListener('load', fitViewport);
  update();
  markToc();
  window.__NAV__ = {
    chapter: CHAPTER, cards: cards, quizzesOf: quizzesOf, currentIndex: currentIndex,
    position: position, chaptersReady: chaptersReady,
    get quiz() { return quiz; }, get restoring() { return restoring; }
  };
})();
