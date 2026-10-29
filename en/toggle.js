/* 中/EN overlay engine for the CCC-LNS lecture pages.
 * Loaded by one injected line per chapter:
 *   <script src="../../en/toggle.js" data-chapter="IDL_115/ChNN-xxx" defer></script>
 * See CLAUDE.md ("How the engine works") for the design. Never edits page JS or files;
 * everything here happens in the live DOM.
 */
(function () {
  'use strict';

  var script = document.currentScript || document.querySelector('script[src*="en/toggle.js"]');
  var CHAPTER = script.getAttribute('data-chapter');
  var BASE = new URL('.', script.src).href;               // .../en/
  var CH_BASE = BASE + CHAPTER + '/';
  var STORE_KEY = 'ccc-lns-lang';

  // ---------- text helpers ----------
  // The whitespace class is spelled out so Python (en/tools/_common.py) matches it exactly.
  var WS = /[ \t\n\r\f\v\u00a0\u3000\u2028\u2029\ufeff]+/g;
  var HAN = /[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]/;
  function normalize(s) { return s.replace(WS, ' ').replace(/^ | $/g, ''); }
  function hasHan(s) { return HAN.test(s); }

  // Synchronous SHA-1 over UTF-8 (no crypto.subtle: capture must finish before KaTeX runs).
  function sha1(str) {
    var bytes = new TextEncoder().encode(str);
    var n = bytes.length, words = ((n + 8) >> 6) + 1, w = new Array(words * 16).fill(0), i;
    for (i = 0; i < n; i++) w[i >> 2] |= bytes[i] << (24 - (i % 4) * 8);
    w[n >> 2] |= 0x80 << (24 - (n % 4) * 8);
    w[words * 16 - 1] = n * 8;
    var h0 = 0x67452301, h1 = 0xefcdab89, h2 = 0x98badcfe, h3 = 0x10325476, h4 = 0xc3d2e1f0;
    var x = new Array(80);
    for (var blk = 0; blk < w.length; blk += 16) {
      for (i = 0; i < 16; i++) x[i] = w[blk + i] | 0;
      for (i = 16; i < 80; i++) { var t = x[i - 3] ^ x[i - 8] ^ x[i - 14] ^ x[i - 16]; x[i] = (t << 1) | (t >>> 31); }
      var a = h0, b = h1, c = h2, d = h3, e = h4;
      for (i = 0; i < 80; i++) {
        var f, k;
        if (i < 20) { f = (b & c) | (~b & d); k = 0x5a827999; }
        else if (i < 40) { f = b ^ c ^ d; k = 0x6ed9eba1; }
        else if (i < 60) { f = (b & c) | (b & d) | (c & d); k = 0x8f1bbcdc; }
        else { f = b ^ c ^ d; k = 0xca62c1d6; }
        var tmp = (((a << 5) | (a >>> 27)) + f + e + k + x[i]) | 0;
        e = d; d = c; c = (b << 30) | (b >>> 2); b = a; a = tmp;
      }
      h0 = (h0 + a) | 0; h1 = (h1 + b) | 0; h2 = (h2 + c) | 0; h3 = (h3 + d) | 0; h4 = (h4 + e) | 0;
    }
    return [h0, h1, h2, h3, h4].map(function (v) { return ('00000000' + (v >>> 0).toString(16)).slice(-8); }).join('');
  }
  function keyOf(text) { return sha1(normalize(text)).slice(0, 12); }

  function htmlToText(html) {
    var t = document.createElement('template'); t.innerHTML = html; return t.content.textContent;
  }

  // ---------- unit collection ----------
  var BLOCK = /^(P|LI|H[1-6]|TD|TH|FIGCAPTION|DIV|SECTION|UL|OL|DL|DT|DD|TABLE|THEAD|TBODY|TFOOT|TR|FIGURE|DETAILS|SUMMARY|PRE|BLOCKQUOTE|NAV|HEADER|FOOTER|MAIN|ARTICLE|ASIDE|FORM|FIELDSET|LEGEND|OPTION|OPTGROUP|HR|BODY)$/;
  var OPAQUE = /^(INPUT|SELECT|TEXTAREA|BUTTON|CANVAS|SVG|IFRAME|VIDEO|AUDIO|IMG|OBJECT|MATH)$/;
  var SKIP_TAG = /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE)$/;
  var SKIP_SEL = '.katex, .ai-illustration, #en-toggle, [data-en-skip]';
  var BOUNDARY_SEL = 'p,li,h1,h2,h3,h4,h5,h6,td,th,figcaption,div,section,ul,ol,dl,dt,dd,table,tr,figure,details,summary,pre,blockquote,nav,header,footer,main,article,aside,form,fieldset,legend,option,hr,' +
    'input,select,textarea,button,canvas,svg,iframe,video,audio,img,object,math,script,style,noscript,template';
  var ATTRS = ['title', 'alt', 'placeholder', 'aria-label'];
  var GUIDE_IDS = { 'guide-title': 1, 'guide-body': 1 };

  var dynamicSel = [];          // from strings.json _dynamic
  var units = [];               // {el, key, zh, text, ctx, kp, attr?, cur}
  var unitEls = new WeakSet();
  var expl = [];                // data-expl values (translated via $T only, never mutated)

  function tag(el) { return el.tagName.toUpperCase(); }
  function isSkipped(el) {
    if (SKIP_TAG.test(tag(el))) return true;
    if (el.matches && el.matches(SKIP_SEL)) return true;
    for (var i = 0; i < dynamicSel.length; i++) if (el.matches(dynamicSel[i])) return true;
    return false;
  }
  function isBoundary(node) {
    if (node.nodeType !== 1) return false;
    var t = tag(node);
    return BLOCK.test(t) || OPAQUE.test(t) || isSkipped(node) || !!node.querySelector(BOUNDARY_SEL);
  }
  function kpOf(el, ctx, guideKp) {
    if (ctx === 'guide') return guideKp;
    var s = el.closest('[data-kp]');
    return s ? parseInt(s.getAttribute('data-kp'), 10) || 0 : 0;
  }
  function addUnit(el, ctx, guideKp) {
    var svg = ctx === 'svg';
    var zh = svg ? el.textContent : el.innerHTML;
    var text = el.textContent;
    if (!hasHan(text)) return;
    var u = { el: el, key: keyOf(text), zh: zh, raw: text, text: normalize(text), ctx: ctx, kp: kpOf(el, ctx, guideKp), cur: 'zh' };
    units.push(u); unitEls.add(el);
  }
  function collectSvg(svg, ctx, guideKp) {
    svg.querySelectorAll('text').forEach(function (t) {
      var spans = t.querySelectorAll('tspan');
      if (spans.length) spans.forEach(function (s) { addUnit(s, 'svg', guideKp); });
      else addUnit(t, 'svg', guideKp);
    });
  }
  // Partition a container's children into boundary children and inline runs.
  function walk(el, ctx, guideKp) {
    if (isSkipped(el)) return;
    if (tag(el) === 'SVG' || el instanceof SVGElement) { collectSvg(el, ctx, guideKp); return; }
    var kids = Array.prototype.slice.call(el.childNodes);
    if (!kids.some(isBoundary) && tag(el) !== 'BODY') { addUnit(el, ctx, guideKp); return; }
    var run = [];
    function flush() {
      var r = run; run = [];
      while (r.length && r[0].nodeType === 3 && !normalize(r[0].data)) r.shift();
      while (r.length && r[r.length - 1].nodeType === 3 && !normalize(r[r.length - 1].data)) r.pop();
      if (!r.length) return;
      var loose = r.some(function (n) { return n.nodeType === 3 && normalize(n.data); });
      if (!loose) { r.forEach(function (n) { if (n.nodeType === 1) addUnit(n, ctx, guideKp); }); return; }
      if (!hasHan(r.map(function (n) { return n.textContent; }).join(''))) return;
      var span = document.createElement('span');
      span.setAttribute('data-en-run', '');
      r[0].parentNode.insertBefore(span, r[0]);
      r.forEach(function (n) { span.appendChild(n); });
      addUnit(span, ctx, guideKp);
    }
    kids.forEach(function (n) {
      if (n.nodeType === 8) return;
      if (isBoundary(n)) { flush(); walk(n, ctx, guideKp); }
      else run.push(n);
    });
    flush();
  }
  function collectAttrs(root, ctx, guideKp) {
    var sel = ATTRS.map(function (a) { return '[' + a + ']'; }).join(',') + ',[data-expl]';
    var els = Array.prototype.slice.call(root.querySelectorAll(sel));
    if (root.matches && root.matches(sel)) els.unshift(root);
    els.forEach(function (el) {
      if (el.closest('script,style,.ai-illustration,#en-toggle,[data-en-skip]')) return;
      ATTRS.forEach(function (a) {
        var v = el.getAttribute(a);
        if (v && hasHan(v)) {
          units.push({ el: el, attr: a, key: keyOf(v), zh: v, raw: v, text: normalize(v), ctx: ctx === 'guide' ? 'guide' : 'attr', kp: kpOf(el, ctx, guideKp), cur: 'zh' });
        }
      });
      var e = el.getAttribute('data-expl');
      if (e && hasHan(e)) expl.push({ el: el, key: keyOf(e), zh: e, raw: e, text: normalize(e), ctx: 'expl', kp: kpOf(el, ctx, guideKp) });
    });
  }

  // ---------- strings ----------
  var S = {}, runtime = { exact: {}, patterns: [] }, images = [], textMap = {}, loaded = false, loadError = null;
  function buildMaps() {
    textMap = {};
    Object.keys(S).forEach(function (k) {
      if (k.charAt(0) === '_') return;
      var e = S[k];
      if (!e || !e.en) return;
      var isHtml = e.ctx !== 'attr' && e.ctx !== 'expl' && e.ctx !== 'svg' && !e.attr;
      textMap[normalize(isHtml ? htmlToText(e.zh) : e.zh)] = isHtml ? htmlToText(e.en) : e.en;
    });
    runtime.compiled = (runtime.patterns || []).map(function (p) { return { re: new RegExp(p.re), en: p.en }; });
  }
  function lookup(s) {
    if (runtime.exact && runtime.exact[s] != null) return runtime.exact[s];
    var t = textMap[normalize(s)];
    return t != null ? t : null;
  }
  function translateLine(line) {
    var m = /^(\s*)([\s\S]*?)(\s*)$/.exec(line), core = m[2];
    if (!hasHan(core)) return null;
    var hit = lookup(core);
    if (hit == null) {
      for (var i = 0; i < runtime.compiled.length; i++) {
        var p = runtime.compiled[i], g = p.re.exec(core);
        if (!g) continue;
        hit = p.en.replace(/\$(T?)(\d)/g, function (_, t, d) {
          var c = g[+d] == null ? '' : g[+d];
          if (!t) return c;
          var tr = lookup(c);
          return tr != null ? tr : c;
        });
        break;
      }
    }
    return hit == null ? null : m[1] + hit + m[3];
  }
  function translateText(s) {
    var changed = false;
    var out = s.split('\n').map(function (l) {
      var t = translateLine(l);
      if (t == null) return l;
      changed = true; return t;
    }).join('\n');
    return changed ? out : null;
  }

  // ---------- state ----------
  var lang = 'zh';
  var misses = [];
  var missSeen = {};
  function miss(where, text, el) {
    var id = where + '|' + text;
    if (missSeen[id]) return;
    missSeen[id] = 1;
    misses.push({ where: where, text: text, path: el ? pathOf(el) : '', kp: el && el.closest ? kpOf(el, 'page') : 0 });
  }
  function pathOf(el) {
    var parts = [];
    while (el && el.nodeType === 1 && parts.length < 5) {
      var p = el.tagName.toLowerCase();
      if (el.id) { parts.unshift(p + '#' + el.id); break; }
      var cls = el.classList ? Array.prototype.filter.call(el.classList, function (c) { return c.indexOf('en-') !== 0; }) : [];
      if (cls.length) p += '.' + cls[0];
      var parent = el.parentElement;
      if (parent) {
        var same = Array.prototype.filter.call(parent.children, function (c) { return c.tagName === el.tagName; });
        if (same.length > 1) p += ':nth-of-type(' + (same.indexOf(el) + 1) + ')';
      }
      parts.unshift(p);
      el = parent;
    }
    return parts.join(' > ');
  }

  // ---------- math ----------
  var MATH_OPTS = {
    delimiters: [
      { left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false },
      { left: '\\(', right: '\\)', display: false }, { left: '\\[', right: '\\]', display: true }
    ],
    throwOnError: false, ignoredClasses: ['katex']
  };
  function renderMath(el) {
    if (window.renderMathInElement) { try { window.renderMathInElement(el, MATH_OPTS); } catch (e) { /* page renders later */ } }
  }
  var MATH_RE = /\$|\\\(|\\\[/;

  // ---------- swapping ----------
  function applyUnit(u, target) {
    var el = u.el;
    if (!el.isConnected) return false;
    if (target === 'en') {
      var t = S[u.key];
      if (!t || !t.en) {
        if (!u.attr && u.ctx !== 'svg') el.classList.add('en-missing');
        return false;
      }
      if (u.cur === 'en') return false;
      if (u.attr) el.setAttribute(u.attr, t.en);
      else if (u.ctx === 'svg') el.textContent = t.en;
      else el.innerHTML = t.en;
      u.cur = 'en';
      return !u.attr && u.ctx !== 'svg' && MATH_RE.test(t.en);
    }
    if (!u.attr && u.ctx !== 'svg') el.classList.remove('en-missing');
    if (u.cur !== 'en') return false;
    if (u.attr) el.setAttribute(u.attr, u.zh);
    else if (u.ctx === 'svg') el.textContent = u.zh;
    else el.innerHTML = u.zh;
    u.cur = 'zh';
    return !u.attr && u.ctx !== 'svg' && MATH_RE.test(u.zh);
  }
  function swapUnits(list, target) {
    var math = [];
    list.forEach(function (u) { if (applyUnit(u, target)) math.push(u.el); });
    math.forEach(renderMath);
  }

  var imgOrig = new WeakMap();
  function swapImages(target) {
    if (!images.length) return;
    document.querySelectorAll('img').forEach(function (img) {
      if (target === 'en') {
        var src = img.getAttribute('src') || '';
        var file = src.split('/').pop().split('?')[0];
        if (images.indexOf(file) < 0 || imgOrig.has(img)) return;
        imgOrig.set(img, src);
        img.setAttribute('src', CH_BASE + 'assets/' + file);
      } else if (imgOrig.has(img)) {
        img.setAttribute('src', imgOrig.get(img));
        imgOrig.delete(img);
      }
    });
  }

  // Runtime (script-generated) text.
  var written = new Map();      // text node -> {zh, en}
  function insideUnit(node) {
    for (var n = node.nodeType === 1 ? node : node.parentNode; n && n !== document.body; n = n.parentNode) {
      if (unitEls.has(n)) return true;
    }
    return false;
  }
  function ignorable(node) {
    var el = node.nodeType === 1 ? node : node.parentElement;
    return !el || !!el.closest('.katex, .ai-illustration, #en-toggle, [data-en-skip], script, style');
  }
  function translateNode(n) {
    if (ignorable(n) || insideUnit(n)) return;
    var rec = written.get(n);
    if (rec && n.data === rec.en) return;
    if (!hasHan(n.data)) return;
    var r = translateText(n.data);
    if (r != null) { written.set(n, { zh: n.data, en: r }); n.data = r; }
    if (hasHan(r != null ? r : n.data)) {
      var bad = (r != null ? r : n.data).split('\n').filter(hasHan).join(' / ');
      miss('runtime', normalize(bad).slice(0, 120), n.parentElement);
    }
  }
  function textNodesIn(root) {
    if (root.nodeType === 3) return [root];
    if (root.nodeType !== 1) return [];
    var out = [], w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    while (w.nextNode()) out.push(w.currentNode);
    return out;
  }
  function runtimePass(target) {
    if (target === 'en') { textNodesIn(document.body).forEach(translateNode); return; }
    written.forEach(function (rec, n) { if (n.isConnected && n.data === rec.en) n.data = rec.zh; });
    written.clear();
  }

  // Canvas: translate text drawn while EN is on.
  var hanCanvases = new Set();
  ['fillText', 'strokeText'].forEach(function (name) {
    var proto = window.CanvasRenderingContext2D && CanvasRenderingContext2D.prototype;
    if (!proto || !proto[name]) return;
    var orig = proto[name];
    proto[name] = function (text) {
      if (typeof text === 'string' && hasHan(text) && this.canvas) hanCanvases.add(this.canvas);
      if (lang === 'en' && typeof text === 'string' && hasHan(text)) {
        var r = translateText(text);
        if (r == null || hasHan(r)) miss('canvas', text, this.canvas);
        if (r != null) { var args = Array.prototype.slice.call(arguments); args[0] = r; return orig.apply(this, args); }
      }
      return orig.apply(this, arguments);
    };
  });
  function redrawDemos() {
    document.querySelectorAll('.demo').forEach(function (d) {
      d.querySelectorAll('input[type=range], input[type=number], select').forEach(function (c) {
        c.dispatchEvent(new Event('input', { bubbles: true }));
        if (tag(c) === 'SELECT') c.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
  }

  // ---------- guides (教授祕笈) ----------
  function guideKpNow() {
    var title = document.getElementById('guide-title'), G = window.__GUIDES__ || {};
    if (!title) return 0;
    var t = normalize(title.textContent);
    for (var k in G) if (G[k] && normalize(G[k].title || '') === t) return parseInt(k, 10) || 0;
    return 0;
  }
  function recaptureGuide() {
    units = units.filter(function (u) { return u.el.isConnected && !(u.ctx === 'guide'); });
    var gk = guideKpNow(), start = units.length;
    ['guide-title', 'guide-body'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) walk(el, 'guide', gk);
    });
    var modal = document.getElementById('guide-modal');
    var fresh = units.slice(start);
    if (lang === 'en') swapUnits(fresh, 'en');
    return modal;
  }

  // ---------- MutationObserver ----------
  var OBS_OPTS = { childList: true, characterData: true, subtree: true };
  var observer = new MutationObserver(handle);
  var swapping = false;
  function isKatexRecord(rec) {
    return Array.prototype.some.call(rec.addedNodes, function (n) {
      return n.nodeType === 1 && (n.matches('.katex, .katex-display') || !!n.querySelector('.katex'));
    });
  }
  function handle(records) {
    if (swapping) return;
    var guideDirty = false, nodes = [];
    records.forEach(function (rec) {
      var t = rec.target;
      if (ignorable(t)) return;
      if (rec.type === 'childList' && t.id && GUIDE_IDS[t.id]) {
        // KaTeX replacing a direct text child also targets the container: not a new guide.
        if (!isKatexRecord(rec)) guideDirty = true;
        return;
      }
      if (insideUnit(t)) return;
      if (rec.type === 'characterData') nodes.push(t);
      else rec.addedNodes.forEach(function (n) { nodes = nodes.concat(textNodesIn(n)); });
    });
    swapping = true;
    try {
      if (guideDirty) recaptureGuide();
      if (lang === 'en' && loaded) nodes.forEach(function (n) { if (n.isConnected) translateNode(n); });
    } finally {
      observer.takeRecords();      // drop the records our own writes just produced
      swapping = false;
    }
  }
  function quiet(fn) {
    var pending = observer.takeRecords();
    if (pending.length) handle(pending);
    observer.disconnect();
    swapping = true;
    try { fn(); } finally {
      swapping = false;
      observer.observe(document.body, OBS_OPTS);
    }
  }

  // ---------- language switch ----------
  function setLang(target, opts) {
    target = target === 'en' ? 'en' : 'zh';
    if (target === 'en' && !loaded) { pendingLang = 'en'; return; }
    quiet(function () {
      lang = target;
      swapUnits(units, target);
      swapImages(target);
      runtimePass(target);
    });
    document.documentElement.setAttribute('lang', target === 'en' ? 'en' : 'zh-Hant');
    document.documentElement.classList.remove('en-pending');
    if (!(opts && opts.noSave)) { try { localStorage.setItem(STORE_KEY, target); } catch (e) { /* storage blocked */ } }
    updateButton();
    redrawDemos();
  }
  var pendingLang = null;

  // ---------- UI ----------
  var CSS = [
    ':root{--en-bg:#ffffff;--en-fg:#1f2430;--en-border:#cbd5e1;--en-on-bg:#0d9488;--en-on-fg:#ffffff;--en-miss:#f59e0b;--en-shadow:0 2px 8px rgba(0,0,0,.15);}',
    '@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--en-bg:#1e293b;--en-fg:#e2e8f0;--en-border:#475569;--en-on-bg:#14b8a6;--en-on-fg:#0f172a;--en-miss:#fbbf24;--en-shadow:0 2px 8px rgba(0,0,0,.5);}}',
    ':root[data-theme="dark"]{--en-bg:#1e293b;--en-fg:#e2e8f0;--en-border:#475569;--en-on-bg:#14b8a6;--en-on-fg:#0f172a;--en-miss:#fbbf24;--en-shadow:0 2px 8px rgba(0,0,0,.5);}',
    '#en-toggle{position:fixed;top:12px;right:12px;z-index:1000;display:flex;padding:3px;gap:2px;border-radius:99px;border:1px solid var(--en-border);background:var(--en-bg);box-shadow:var(--en-shadow);cursor:pointer;font:600 13px/1 system-ui,-apple-system,"Segoe UI",sans-serif;}',
    '#en-toggle span{padding:6px 11px;border-radius:99px;color:var(--en-fg);}',
    '#en-toggle span.on{background:var(--en-on-bg);color:var(--en-on-fg);}',
    '#en-toggle:focus-visible{outline:2px solid var(--en-on-bg);outline-offset:2px;}',
    '.en-missing{outline:2px dashed var(--en-miss)!important;outline-offset:2px;}',
    'html.en-pending header, html.en-pending main{visibility:hidden;}'
  ].join('\n');
  var btn;
  function buildUi() {
    var st = document.createElement('style'); st.id = 'en-toggle-style'; st.textContent = CSS;
    document.head.appendChild(st);
    btn = document.createElement('button');
    btn.id = 'en-toggle'; btn.type = 'button';
    btn.title = '中 / EN (Alt+L)';
    btn.innerHTML = '<span data-l="zh">中</span><span data-l="en">EN</span>';
    btn.addEventListener('click', function () { setLang(lang === 'en' ? 'zh' : 'en'); });
    document.body.appendChild(btn);
    document.addEventListener('keydown', function (e) {
      if (e.altKey && !e.ctrlKey && !e.metaKey && e.code === 'KeyL') { e.preventDefault(); setLang(lang === 'en' ? 'zh' : 'en'); }
    });
    updateButton();
  }
  function updateButton() {
    if (!btn) return;
    btn.querySelectorAll('span').forEach(function (s) { s.classList.toggle('on', s.getAttribute('data-l') === lang); });
    btn.setAttribute('aria-label', lang === 'en' ? 'Language: English. Switch to Chinese' : '語言：中文。切換為英文');
  }

  // ---------- boot ----------
  var saved = 'en';                                        // English unless 中 was chosen
  try { saved = localStorage.getItem(STORE_KEY) === 'zh' ? 'zh' : 'en'; } catch (e) { /* storage blocked */ }
  if (saved === 'en') {
    document.documentElement.classList.add('en-pending');
    setTimeout(function () { document.documentElement.classList.remove('en-pending'); }, 1500);
  }

  // The whole page is parsed and KaTeX has not rendered yet: capture now, synchronously.
  // _dynamic selectors are only known once strings.json arrives, so capture with the
  // chapter's defaults first and drop units that fall inside _dynamic afterwards.
  walk(document.body, 'page', 0);
  collectAttrs(document.body, 'page', 0);
  buildUi();
  observer.observe(document.body, OBS_OPTS);

  var api = window.__EN__ = {
    chapter: CHAPTER, ready: false, misses: misses,
    get lang() { return lang; },
    get loadError() { return loadError; },
    hanCanvases: function () { return Array.from(hanCanvases).filter(function (c) { return c.isConnected; }); },
    setLang: setLang, normalize: normalize, sha1: sha1, keyOf: keyOf, translateText: translateText,
    collect: function () {
      return units.concat(expl).filter(function (u) { return u.el.isConnected; }).map(function (u) {
        var t = S[u.key];
        return {
          key: u.key, raw: u.raw, text: u.text, zh: u.zh, ctx: u.ctx, kp: u.kp, attr: u.attr || null,
          path: pathOf(u.el), translated: !!(t && t.en), cur: u.cur || 'zh'
        };
      });
    }
  };

  fetch(CH_BASE + 'strings.json', { cache: 'no-cache' }).then(function (r) {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  }).then(function (data) {
    S = data || {};
    runtime = S._runtime || { exact: {}, patterns: [] };
    images = S._images || [];
    dynamicSel = S._dynamic || [];
    if (dynamicSel.length) {
      var drop = function (u) { return dynamicSel.some(function (s) { return u.el.closest(s); }); };
      units = units.filter(function (u) {
        if (u.attr || !drop(u)) return true;
        unitEls.delete(u.el); return false;
      });
    }
    buildMaps();
  }).catch(function (e) { loadError = String(e); buildMaps(); }).then(function () {
    loaded = true; api.ready = true;
    if (saved === 'en' || pendingLang === 'en') setLang('en', { noSave: pendingLang !== 'en' });
    else document.documentElement.classList.remove('en-pending');
  });
})();
