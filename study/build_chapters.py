"""Rebuild study/chapters.json (the dashboard's chapter list) from the IDL_115/ folders.

    python3 study/build_chapters.py [--check]

Standard library only, so /sync-upstream can run it without the venv. Reads the professor's
files but never writes them. --check exits 1 if chapters.json is out of date.
"""
import argparse
import hashlib
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
COURSE = 'IDL_115'
OUT = REPO / 'study' / 'chapters.json'
TITLES = REPO / 'study' / 'titles_en.json'

# Quiz containers in the four page families (see CLAUDE.md, "Study layer"). Must match
# QUIZ_SEL in en/nav.js so quiz indexes agree.
QUIZ_CLASSES = {'quiz', 'quiz-container', 'quiz-sec'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
        'source', 'track', 'wbr'}

# Same normalize/key as en/toggle.js and en/tools/_common.py (kept inline: stdlib only).
WS = re.compile('[ \t\n\r\f\v 　  ﻿]+')


def normalize(s):
    s = WS.sub(' ', s)
    if s.startswith(' '):
        s = s[1:]
    if s.endswith(' '):
        s = s[:-1]
    return s


def key_of(text):
    return hashlib.sha1(normalize(text).encode('utf-8')).hexdigest()[:12]


class Sections(HTMLParser):
    """Collect section.card[data-kp] with their badge, heading text and quiz count."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, role) where role in {None, 'section', 'title', 'badge', 'quiz'}
        self.sections = []
        self.cur = None
        self.buf = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get('class') or '').split())
        roles = {r for _, r in self.stack}
        role = None
        if tag == 'section' and 'card' in cls and a.get('data-kp') and re.fullmatch(r'kp\d+', a.get('id') or ''):
            self.cur = {'kp': int(a['data-kp']), 'id': a['id'], 'badge': '', 'zh': '', 'quizzes': 0}
            self.sections.append(self.cur)
            role = 'section'
        elif self.cur and 'quiz' not in roles:
            if cls & QUIZ_CLASSES:
                self.cur['quizzes'] += 1
                role = 'quiz'
            elif not self.cur['zh'] and 'title' not in roles and (
                    'card-title' in cls or (tag == 'h3' and 'head' in roles)):
                role, self.buf = 'title', []
            elif not self.cur['badge'] and cls & {'badge', 'card-badge'}:
                role, self.buf = 'badge', []
            elif cls & {'card-head', 'card-header'}:
                role = 'head'
        if tag not in VOID:
            self.stack.append((tag, role))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for _, role in self.stack[i:]:
                    if role in ('title', 'badge') and self.buf is not None:
                        self.cur['zh' if role == 'title' else 'badge'] = ''.join(self.buf)
                        self.buf = None
                    elif role == 'section':
                        self.cur = None
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.buf is not None:
            self.buf.append(data)


def plain(s):
    return normalize(html.unescape(re.sub(r'<[^>]+>', '', s))).strip()


SLIDE_WORDS = {w: w.upper() for w in 'ml ai cnn mlp uat sgd sam rbf som xor rl dr pca gap fft'.split()}
SLIDE_WORDS.update({'mp': 'M-P', 'adagrad': 'AdaGrad', 'rmsprop': 'RMSProp', 'imagenet': 'ImageNet',
                    'ilsvrc': 'ILSVRC', 'alexnet': 'AlexNet', 'vgg': 'VGG', 'googlenet': 'GoogLeNet',
                    'unet': 'U-Net', 'resnet': 'ResNet', 'densenet': 'DenseNet', 'lenet': 'LeNet',
                    'adaline': 'ADALINE', 'chapter3': 'chapter 3', 'chapter4': 'chapter 4',
                    'vs': 'vs.', 'and': 'and', 'to': 'to'})


def page_en(pid):
    """translated/units of a deck or slide page, or None when it has no overlay yet."""
    f = REPO / 'en' / (pid + '/strings.json')
    if not f.exists():
        return None
    units = [v for k, v in json.loads(f.read_text(encoding='utf-8')).items() if not k.startswith('_')]
    return {'units': len(units), 'translated': sum(1 for v in units if v.get('en'))}


def slide_label(name):
    m = re.match(r'(\d+)-(.*)\.html$', name)
    num, slug = (m.group(1), m.group(2)) if m else ('', name[:-5])
    slug = re.sub(r'-bilingual$', '', slug)
    words = [SLIDE_WORDS.get(w, w) for w in slug.split('-')]
    text = ' '.join(words)
    text = text[:1].upper() + text[1:]
    return f'{num} {text}'.strip()


def chapter_entry(d, titles, warnings):
    cid = d.name
    rel = f'{COURSE}/{cid}'
    page = (d / 'index.html').read_text(encoding='utf-8')
    p = Sections()
    p.feed(page)
    p.close()

    strings_file = REPO / 'en' / COURSE / cid / 'strings.json'
    S = json.loads(strings_file.read_text(encoding='utf-8')) if strings_file.exists() else {}
    units = {k: v for k, v in S.items() if not k.startswith('_')}

    sections = []
    for s in p.sections:
        t = units.get(key_of(s['zh']))
        sections.append({
            'kp': s['kp'], 'id': s['id'], 'badge': plain(s['badge']),
            'title': plain(t['en']) if t and t.get('en') else None,
            'quizzes': s['quizzes'],
        })
    if not sections:
        warnings.append(f'{cid}: no section.card[data-kp] found')

    title = titles.get(cid)
    if not title:
        title = re.sub(r'^Ch\d+-', '', cid).replace('-', ' ').title()
        warnings.append(f'{cid}: no English title in study/titles_en.json, using "{title}"')

    decks = sorted(f.name for f in d.glob('*.html') if f.name != 'index.html')
    slides = sorted((d / 'slides').glob('*.html')) if (d / 'slides').is_dir() else []
    m = re.match(r'Ch(\d+)', cid)
    return {
        'id': cid,
        'num': int(m.group(1)) if m else None,
        'title': title,
        'lecture': f'{rel}/index.html',
        'decks': [{'href': f'{rel}/{n}', 'en': page_en(f'{rel}/{n[:-5]}')} for n in decks],
        'slides': [{'label': slide_label(f.name), 'href': f'{rel}/slides/{f.name}',
                    'en': page_en(f'{rel}/slides/{f.stem}')} for f in slides],
        'sections': sections,
        'quizzes': sum(s['quizzes'] for s in sections),
        'en': {
            'units': len(units),
            'translated': sum(1 for v in units.values() if v.get('en')),
            'review': sum(1 for v in units.values() if v.get('review')),
            'stale': len(S.get('_stale') or []),
            'toggle': 'en/toggle.js' in page,
        },
        'nav': 'en/nav.js' in page,
    }


def build():
    titles = json.loads(TITLES.read_text(encoding='utf-8'))
    warnings = []
    dirs = sorted(d for d in (REPO / COURSE).iterdir() if (d / 'index.html').is_file())
    data = {'course': COURSE, 'chapters': [chapter_entry(d, titles, warnings) for d in dirs]}
    return json.dumps(data, ensure_ascii=False, indent=1) + '\n', data, warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='exit 1 if chapters.json is out of date')
    args = ap.parse_args()
    text, data, warnings = build()
    for w in warnings:
        print('warning:', w, file=sys.stderr)
    if args.check:
        ok = OUT.exists() and OUT.read_text(encoding='utf-8') == text
        print('chapters.json', 'up to date' if ok else 'OUT OF DATE')
        sys.exit(0 if ok else 1)
    old = OUT.read_text(encoding='utf-8') if OUT.exists() else None
    OUT.write_text(text, encoding='utf-8')
    chs = data['chapters']
    print(f'chapters.json: {len(chs)} chapters, {sum(len(c["sections"]) for c in chs)} sections, '
          f'{sum(c["quizzes"] for c in chs)} quizzes{" (unchanged)" if old == text else ""}')
    for c in chs:
        en = c['en']
        st = f'{en["translated"]}/{en["units"]}' if en['units'] else '-'
        print(f'  {c["id"]:<46} sec {len(c["sections"]):>2}  quiz {c["quizzes"]:>3}  '
              f'slides {len(c["slides"]):>2}  decks {len(c["decks"])}  en {st}{"  nav" if c["nav"] else ""}')


if __name__ == '__main__':
    main()
