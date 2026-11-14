"""Writes the user guide pages from tools/pages_*.py into src/content/docs.

Each page is a dict: sec, slug, order, and per language (en, nl) a title,
a description and a Markdown body. Tokens in the body:
  {{img:name|alt}}   a screenshot from src/assets/screens/name.webp
  {{link:sec/slug}}  a link to another guide page in the same language
Run:  python3 tools/gen.py
Afterwards the .md files can be edited directly; this script is only the
starting point and does not need to be run again.
"""
import importlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'src', 'content', 'docs')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MODULES = ['pages_start', 'pages_map', 'pages_spots', 'pages_field', 'pages_rules', 'pages_settings', 'pages_travel', 'pages_help', 'pages_about']


TITLES = {}

# Translations beyond en and nl: tools/tr/<lang>/<module>.py, each with
# T = {'sec/slug': {'title', 'desc', optional 'label', 'body'}}. A page that
# is missing there simply shows the English text with Starlight's notice.
EXTRA = ['de', 'pt', 'da', 'fr', 'it', 'es']


def load_extra(name):
    out = {}
    for lang in EXTRA:
        try:
            out[lang] = importlib.import_module(f'tr.{lang}.{name}').T
        except ModuleNotFoundError:
            pass
    return out


def render(body, lang):
    depth = 4 if lang == 'en' else 5
    up = '../' * depth
    pre = '/' if lang == 'en' else f'/{lang}/'
    body = re.sub(r'\{\{img:([a-z0-9-]+)\|([^}]*)\}\}', lambda m: f'![{m.group(2)}]({up}assets/screens/{m.group(1)}.webp)', body)
    def link(m):
        key = m.group(1)
        title = TITLES.get((key, lang)) or TITLES.get((key, 'en'))
        if title is None:
            raise SystemExit(f'unknown link {key} ({lang})')
        return f'[{title}]({pre}guide/{key}/)'
    body = re.sub(r'\{\{link:([a-z0-9/-]+)\}\}', link, body)
    return body.strip() + '\n'


def yaml_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def main():
    count = 0
    mods = []
    for name in MODULES:
        try:
            mods.append(importlib.import_module(name))
        except ModuleNotFoundError:
            pass
    for mod in mods:
        for lang, tr in load_extra(mod.__name__).items():
            for p in mod.PAGES:
                key = p['sec'] + '/' + p['slug']
                if key in tr:
                    p[lang] = tr[key]
    for mod in mods:
        for p in mod.PAGES:
            for lang in ['en', 'nl'] + EXTRA:
                if lang in p:
                    TITLES[(p['sec'] + '/' + p['slug'], lang)] = p[lang].get('label', p[lang]['title'])
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except ModuleNotFoundError:
            continue
        for p in mod.PAGES:
            for lang in ['en', 'nl'] + EXTRA:
                if lang not in p:
                    continue
                d = p[lang]
                folder = os.path.join(DOCS, *(([] if lang == 'en' else [lang]) + ['guide', p['sec']]))
                os.makedirs(folder, exist_ok=True)
                fm = f"---\ntitle: {yaml_str(d['title'])}\ndescription: {yaml_str(d['desc'])}\nsidebar:\n  order: {p['order']}\n"
                if 'label' in d:
                    fm += f"  label: {yaml_str(d['label'])}\n"
                fm += '---\n\n'
                with open(os.path.join(folder, p['slug'] + '.md'), 'w', encoding='utf-8') as f:
                    f.write(fm + render(d['body'], lang))
                count += 1
    print(count, 'pages written')


if __name__ == '__main__':
    main()
