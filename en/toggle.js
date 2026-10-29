/* 中/EN overlay engine for the CCC-LNS lecture pages and slide decks.
 * Loaded by one injected line per page (data-chapter = page id, see en/tools/_common.py):
 *   <script src="../../en/toggle.js" data-chapter="IDL_115/ChNN-xxx" defer></script>
 * On MathJax pages the line has no defer and sits right after the page's MathJax config, so
 * the startup typeset can be held back until the units are captured (see boot()).
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

  // MathJax pages: the config object exists but the loader has not run yet. Stop its startup
  // typeset; boot() captures the raw $...$ source first and then typesets.
  var MJ_HELD = !!(window.MathJax && !window.MathJax.version);
  if (MJ_HELD) { window.MathJax.startup = window.MathJax.startup || {}; window.MathJax.startup.typeset = false; }

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
  var SKIP_SEL = '.katex, mjx-container, .ai-illustration, #en-toggle, [data-en-skip]';
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
  // Pages without data-kp (slide decks): the section number is the 1-based index of the
  // enclosing <section> in document order.
  var sectionIdx = null;
  function kpOf(el, ctx, guideKp) {
    if (ctx === 'guide') return guideKp;
    if (sectionIdx) {
      for (var sec = el.closest('section, .section'); sec; sec = sec.parentElement && sec.parentElement.closest('section, .section')) {
        if (sectionIdx.has(sec)) return sectionIdx.get(sec);
      }
      return 0;
    }
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
  var S = {}, runtime = { exact: {}, patterns: [] }, images = [], hide = [], textMap = {}, loaded = false, loadError = null;
  function buildMaps() {
    textMap = {};
    Object.keys(S).forEach(function (k) {
      if (k.charAt(0) === '_') return;
      var e = S[k];
      if (!e || !e.en) return;
      var isHtml = e.ctx !== 'attr' && e.ctx !== 'expl' && e.ctx !== 'svg' && e.ctx !== 'chart' && !e.attr;
      textMap[canonMath(normalize(isHtml ? htmlToText(e.zh) : e.zh))] = isHtml ? htmlToText(e.en) : e.en;
    });
    runtime.compiled = (runtime.patterns || []).map(function (p) { return { re: new RegExp(p.re), en: p.en }; });
  }
  // \(x\) and $x$ (\[x\] and $$x$$) compare equal: text rebuilt from rendered math uses $.
  function canonMath(s) {
    return s.replace(/\\\[([\s\S]+?)\\\]/g, function (_, m) { return '$$' + m + '$$'; })
            .replace(/\\\(([\s\S]+?)\\\)/g, function (_, m) { return '$' + m + '$'; });
  }
  function lookup(s) {
    if (runtime.exact && runtime.exact[s] != null) return runtime.exact[s];
    var t = textMap[canonMath(normalize(s))];
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
  // MathJax: nothing is typeset before releaseMathJax() (held pages), and every typeset is
  // queued on MathJax.startup.promise, because overlapping typesets break on replaced nodes.
  var mjReleased = !MJ_HELD;
  function mathJax() { return window.MathJax && window.MathJax.typesetPromise ? window.MathJax : null; }
  function mjQueue(fn) {
    var mj = mathJax();
    if (!mj || !mjReleased) return;
    var p = (mj.startup && mj.startup.promise) || Promise.resolve();
    mj.startup.promise = p.then(fn).catch(function () { /* keep the queue alive */ });
  }
  function renderMath(el) {
    if (window.renderMathInElement) { try { window.renderMathInElement(el, MATH_OPTS); } catch (e) { /* page renders later */ } }
  }
  function renderMathAll(els) {
    if (!els.length) return;
    if (window.MathJax && (window.MathJax.version || MJ_HELD)) {
      mjQueue(function () { return window.MathJax.typesetPromise(els.filter(function (e) { return e.isConnected; })); });
      return;
    }
    els.forEach(renderMath);
  }
  // Swap a unit's innerHTML but keep its live [id] elements (e.g. <output id=…> inside a
  // <label>): page scripts cache those nodes, so the new copies are replaced by the originals.
  function setHtmlKeepIds(el, html) {
    var live = {};
    el.querySelectorAll('[id]').forEach(function (n) { live[n.id] = n; });
    el.innerHTML = html;
    el.querySelectorAll('[id]').forEach(function (n) {
      var old = live[n.id];
      if (old && old !== n) { n.replaceWith(old); old.setAttribute('data-en-live', ''); }
    });
  }
  // MathJax keeps a list of typeset items per node; drop them before replacing the content.
  function clearMath(el) {
    var mj = mathJax();
    if (mj && mj.typesetClear && mjReleased) { try { mj.typesetClear([el]); } catch (e) { /* ignore */ } }
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
      else { clearMath(el); setHtmlKeepIds(el, t.en); }
      u.cur = 'en';
      return !u.attr && u.ctx !== 'svg' && MATH_RE.test(t.en);
    }
    if (!u.attr && u.ctx !== 'svg') el.classList.remove('en-missing');
    if (u.cur !== 'en') return false;
    if (u.attr) el.setAttribute(u.attr, u.zh);
    else if (u.ctx === 'svg') el.textContent = u.zh;
    else { clearMath(el); setHtmlKeepIds(el, u.zh); }
    u.cur = 'zh';
    return !u.attr && u.ctx !== 'svg' && MATH_RE.test(u.zh);
  }
  function swapUnits(list, target) {
    var math = [];
    list.forEach(function (u) { if (applyUnit(u, target)) math.push(u.el); });
    renderMathAll(math);
  }

  // _images: a file basename (img src="assets/x.png"), or {key, file} for an inline data: URI,
  // key = sha1(src)[:12] (en/tools/extract.py prints it). The English file is in assets/.
  var imgOrig = new WeakMap(), dataKeys = new WeakMap();
  function imageFile(img, src) {
    if (src.slice(0, 5) !== 'data:') {
      var base = src.split('/').pop().split('?')[0];
      return images.indexOf(base) >= 0 ? base : null;
    }
    if (!dataKeys.has(img)) dataKeys.set(img, sha1(src).slice(0, 12));
    var k = dataKeys.get(img);
    for (var i = 0; i < images.length; i++) if (images[i] && images[i].key === k) return images[i].file;
    return null;
  }
  function swapImages(target) {
    if (!images.length) return;
    document.querySelectorAll('img').forEach(function (img) {
      if (target === 'en') {
        var src = img.getAttribute('src') || '';
        if (imgOrig.has(img)) return;
        var file = imageFile(img, src);
        if (!file) return;
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
  // A live [id] element kept across a swap (setHtmlKeepIds) is written by page scripts, so the
  // text inside it is runtime text even though it sits inside a unit.
  function insideUnit(node) {
    for (var n = node.nodeType === 1 ? node : node.parentNode; n && n !== document.body; n = n.parentNode) {
      if (n.nodeType === 1 && n.hasAttribute('data-en-live')) return false;
      if (unitEls.has(n)) return true;
    }
    return false;
  }
  function ignorable(node) {
    var el = node.nodeType === 1 ? node : node.parentElement;
    return !el || !!el.closest('.katex, mjx-container, .ai-illustration, #en-toggle, [data-en-skip], script, style');
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
  // Script-written text whose math the page renders right away (e.g. quiz feedback written
  // with innerHTML and then renderMath()) reaches us already split around .katex nodes, so the
  // line is rebuilt with each formula's TeX source, translated whole, written back as text and
  // re-rendered.
  var mathWritten = new Map();  // element -> {zh, en} (raw text with $...$)
  function rawWithMath(el) {
    var out = '';
    el.childNodes.forEach(function (n) {
      if (n.nodeType === 3) { out += n.data; return; }
      if (n.nodeType !== 1) return;
      var k = n.classList.contains('katex-display') ? n : n.classList.contains('katex') ? n : null;
      if (!k) { out += rawWithMath(n); return; }
      var a = k.querySelector('annotation[encoding="application/x-tex"]');
      var display = k.classList.contains('katex-display');
      out += a ? (display ? '$$' + a.textContent + '$$' : '$' + a.textContent + '$') : k.textContent;
    });
    return out;
  }
  function mathTargets(root) {
    var set = new Set();
    root.querySelectorAll('.katex').forEach(function (k) {
      var outer = k.parentElement && k.parentElement.closest('.katex-display') || k;
      var el = outer.parentElement;
      if (el && !ignorable(el) && !insideUnit(el)) set.add(el);
    });
    return set;
  }
  function translateMathEl(el) {
    var raw = rawWithMath(el), rec = mathWritten.get(el);
    if (rec && raw === rec.en) return;
    if (!hasHan(raw)) return;
    var r = translateText(raw);
    if (r == null || hasHan(r)) miss('runtime', normalize(r != null ? r : raw).slice(0, 120), el);
    if (r == null) return;
    mathWritten.set(el, { zh: raw, en: r });
    el.textContent = r;
    renderMath(el);
  }
  function runtimePass(target) {
    if (target === 'en') {
      var targets = mathTargets(document.body);
      targets.forEach(translateMathEl);
      textNodesIn(document.body).forEach(function (n) {
        for (var p = n.parentElement; p; p = p.parentElement) if (targets.has(p)) return;
        translateNode(n);
      });
      return;
    }
    written.forEach(function (rec, n) { if (n.isConnected && n.data === rec.en) n.data = rec.zh; });
    written.clear();
    mathWritten.forEach(function (rec, el) {
      if (el.isConnected && rawWithMath(el) === rec.en) { el.textContent = rec.zh; renderMath(el); }
    });
    mathWritten.clear();
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

  // ---------- Chart.js ----------
  // Labels are translated in the chart's own config (Chart.js measures text before drawing,
  // so translating only fillText would break the layout). Existing charts are walked on every
  // switch; charts created or updated later go through a global plugin.
  var chartOrig = new WeakMap();      // config object or array -> {key: {zh, en}}
  function charts() {
    var C = window.Chart;
    return C && C.instances ? Object.keys(C.instances).map(function (k) { return C.instances[k]; }) : [];
  }
  function walkConfig(o, visit, depth) {
    if (!o || depth > 10) return;
    var proto = Object.getPrototypeOf(o);                 // Chart.js builds scales with Object.create(null)
    var plain = Array.isArray(o) || proto === Object.prototype || proto === null;
    if (!plain) return;
    Object.keys(o).forEach(function (k) {
      var v = o[k];
      if (typeof v === 'string') visit(o, k, v);
      else if (v && typeof v === 'object') walkConfig(v, visit, depth + 1);
    });
  }
  function chartConfig(ch) { return ch.config && (ch.config._config || ch.config); }
  function translateChart(ch, target) {
    var changed = false;
    walkConfig(chartConfig(ch), function (o, k, v) {
      var rec = chartOrig.get(o);
      if (target === 'en') {
        if (!hasHan(v)) return;
        var r = translateText(v);
        if (r == null || hasHan(r)) miss('chart', v, ch.canvas);
        if (r == null) return;
        if (!rec) chartOrig.set(o, rec = {});
        rec[k] = { zh: v, en: r }; o[k] = r; changed = true;
      } else if (rec && rec[k]) {
        if (v === rec[k].en) { o[k] = rec[k].zh; changed = true; }
        delete rec[k];
      }
    }, 0);
    return changed;
  }
  function swapCharts(target) {
    charts().forEach(function (ch) { if (translateChart(ch, target)) { try { ch.update('none'); } catch (e) { /* ignore */ } } });
  }
  function hookCharts() {
    if (!window.Chart || !window.Chart.register) return;
    window.Chart.register({ id: 'enOverlay', beforeUpdate: function (ch) { if (lang === 'en' && loaded) translateChart(ch, 'en'); } });
  }
  function chartUnits() {
    var out = [];
    charts().forEach(function (ch) {
      walkConfig(chartConfig(ch), function (o, k, v) {
        var rec = chartOrig.get(o), zh = rec && rec[k] && v === rec[k].en ? rec[k].zh : v;
        if (!hasHan(zh)) return;
        out.push({ key: keyOf(zh), raw: zh, text: normalize(zh), zh: zh, ctx: 'chart', kp: ch.canvas ? kpOf(ch.canvas, 'page') : 0,
          attr: null, path: ch.canvas ? pathOf(ch.canvas) : '', translated: !!(S[keyOf(zh)] && S[keyOf(zh)].en), cur: zh === v ? 'zh' : 'en' });
      }, 0);
    });
    return out;
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
    var guideDirty = false, nodes = [], mathEls = new Set();
    records.forEach(function (rec) {
      var t = rec.target;
      if (ignorable(t)) return;
      if (rec.type === 'childList' && t.id && GUIDE_IDS[t.id]) {
        // KaTeX replacing a direct text child also targets the container: not a new guide.
        if (!isKatexRecord(rec)) guideDirty = true;
        return;
      }
      if (insideUnit(t)) return;
      if (rec.type === 'childList' && isKatexRecord(rec)) { mathEls.add(t.closest('.katex-display') ? t.closest('.katex-display').parentElement : t); return; }
      if (rec.type === 'characterData') nodes.push(t);
      else rec.addedNodes.forEach(function (n) { nodes = nodes.concat(textNodesIn(n)); });
    });
    swapping = true;
    try {
      if (guideDirty) recaptureGuide();
      if (lang === 'en' && loaded) {
        mathEls.forEach(function (el) { if (el.isConnected) translateMathEl(el); });
        nodes.forEach(function (n) {
          if (!n.isConnected) return;
          for (var p = n.parentElement; p; p = p.parentElement) if (mathEls.has(p)) return;
          translateNode(n);
        });
      }
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
      swapCharts(target);
    });
    document.documentElement.classList.toggle('en-on', target === 'en');
    document.documentElement.setAttribute('lang', target === 'en' ? 'en' : 'zh-Hant');
    document.documentElement.classList.remove('en-pending');
    if (!(opts && opts.noSave)) { try { localStorage.setItem(STORE_KEY, target); } catch (e) { /* storage blocked */ } }
    updateButton();
    placeButton();              // the body may just have become visible (en-pending)
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
    'html.en-pending body{visibility:hidden;}',
    'html.en-pending #en-toggle{visibility:visible;}'
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
    placeButton();
    window.addEventListener('load', placeButton);
    window.addEventListener('resize', placeButton);
    document.addEventListener('keydown', function (e) {
      if (e.altKey && !e.ctrlKey && !e.metaKey && e.code === 'KeyL') { e.preventDefault(); setLang(lang === 'en' ? 'zh' : 'en'); }
    });
    updateButton();
  }
  // Decks have their own fixed controls in the top-right corner (theme switch): sit left of them.
  function placeButton() {
    if (!btn) return;
    btn.style.right = '12px';
    for (var tries = 0; tries < 4; tries++) {
      var r = btn.getBoundingClientRect(), hit = null;
      var pts = [];
      [r.left + 2, r.left + r.width / 2, r.right - 2].forEach(function (x) {
        [r.top + 2, r.top + r.height / 2, r.bottom - 2].forEach(function (y) { pts.push([x, y]); });
      });
      pts.some(function (pt) {
        return document.elementsFromPoint(pt[0], pt[1]).some(function (el) {
          if (el === btn || btn.contains(el) || el === document.documentElement || el === document.body) return false;
          for (var n = el; n && n !== document.body; n = n.parentElement) {
            if (getComputedStyle(n).position === 'fixed') { hit = n; return true; }
          }
          return false;
        });
      });
      if (!hit) return;
      var hr = hit.getBoundingClientRect();
      if (hr.width > window.innerWidth / 2) return;        // a full-width bar: nothing to dodge
      btn.style.right = (window.innerWidth - hr.left + 8) + 'px';
    }
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

  // The whole page is parsed and math has not rendered yet: capture now, synchronously.
  // _dynamic selectors are only known once strings.json arrives, so capture with the
  // chapter's defaults first and drop units that fall inside _dynamic afterwards.
  function boot() {
    if (!document.querySelector('[data-kp]')) {
      sectionIdx = new Map();
      var n = 0;
      document.querySelectorAll('section, .section').forEach(function (s) {
        if (!s.parentElement.closest('section, .section')) sectionIdx.set(s, ++n);   // outermost only
      });
    }
    walk(document.body, 'page', 0);
    collectAttrs(document.body, 'page', 0);
    buildUi();
    hookCharts();
    observer.observe(document.body, OBS_OPTS);
    load();
  }
  // Held MathJax pages: the first typeset runs once, after the initial language is applied.
  function releaseMathJax() {
    mjReleased = true;
    var go = function () { return window.MathJax.typesetPromise().catch(function () { /* ignore */ }); };
    var mj = window.MathJax;
    if (mj.version && mj.startup && mj.startup.promise) { mj.startup.promise = mj.startup.promise.then(go); return; }
    var prev = mj.startup.ready;
    mj.startup.ready = function () {
      if (prev) prev(); else window.MathJax.startup.defaultReady();
      window.MathJax.startup.promise = window.MathJax.startup.promise.then(go);
    };
  }

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
      }).concat(chartUnits());
    },
    // Visible leaf blocks with English but no Chinese, outside units and not hidden: the
    // professor's own English, which EN mode shows as is (review it; add pairs to _hide).
    englishOnly: function () {
      var out = [];
      document.body.querySelectorAll('*').forEach(function (el) {
        if (isSkipped(el) || el.closest(SKIP_SEL) || insideUnit(el) || unitEls.has(el)) return;
        if (Array.prototype.some.call(el.childNodes, isBoundary)) return;
        if (!/[A-Za-z]{3,}.*[A-Za-z]{3,}/.test(el.textContent) || hasHan(el.textContent) || !el.getClientRects().length) return;
        if (el.parentElement && !Array.prototype.some.call(el.parentElement.childNodes, isBoundary) && !insideUnit(el.parentElement) &&
            el.parentElement !== document.body) return;          // report the block, not each inline child
        out.push({ path: pathOf(el), kp: kpOf(el, 'page'), text: normalize(el.textContent).slice(0, 160),
          cls: el.className && typeof el.className === 'string' ? el.className : '' });
      });
      return out;
    }
  };

  function load() {
  fetch(CH_BASE + 'strings.json', { cache: 'no-cache' }).then(function (r) {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  }).then(function (data) {
    S = data || {};
    runtime = S._runtime || { exact: {}, patterns: [] };
    images = S._images || [];
    hide = S._hide || [];
    if (hide.length) {
      var st = document.createElement('style'); st.id = 'en-hide-style';
      st.textContent = hide.map(function (h) { return 'html.en-on ' + h; }).join(',\n') + '{display:none!important;}';
      document.head.appendChild(st);
    }
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
    if (MJ_HELD) releaseMathJax();
  });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
