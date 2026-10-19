"""Compose section SVGs into continuous desktop/mobile README canvases."""
from copy import deepcopy
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def compose(mobile=False):
    width = 500 if mobile else 1000
    if mobile:
        sections = [
            ('readme-hero-mobile', 0, 0, 500, 840),
            ('clipdeck-banner-mobile', 0, 840, 500, 680),
            ('project-whisper', 0, 1520, 500, 320),
            ('project-aetherdb', 0, 1840, 500, 320),
            ('project-argus', 0, 2160, 500, 320),
            ('project-syskit', 0, 2480, 500, 320),
            ('engineering-approach-mobile', 0, 2800, 500, 656),
            ('contact-console-mobile', 0, 3456, 500, 296),
        ]
        height = 3752
    else:
        sections = [
            ('readme-hero', 0, 0, 1000, 475),
            ('clipdeck-banner', 0, 475, 1000, 375),
            ('project-whisper', 30, 850, 470, 301),
            ('project-aetherdb', 500, 850, 470, 301),
            ('project-argus', 30, 1151, 470, 301),
            ('project-syskit', 500, 1151, 470, 301),
            ('engineering-approach', 0, 1460, 1000, 315),
            ('contact-console', 0, 1775, 1000, 248),
        ]
        height = 2023
    out = ET.Element(f'{{{NS}}}svg', {'width': str(width), 'height': str(height),
        'viewBox': f'0 0 {width} {height}', 'role': 'img', 'aria-labelledby': 'title desc'})
    ET.SubElement(out, f'{{{NS}}}title', {'id': 'title'}).text = 'Mersad Moghaddam — Software developer portfolio'
    ET.SubElement(out, f'{{{NS}}}desc', {'id': 'desc'}).text = (
        'Go and Linux software developer. Selected work: ClipDeck, Whisper Social, '
        'AetherDB, Argus and SysKit. Understand the problem, make deliberate choices, '
        'and learn through building. Project and contact links follow this illustration.')
    ET.SubElement(out, f'{{{NS}}}rect', {'width': str(width), 'height': str(height), 'fill': '#090D15'})
    for i, (name, x, y, w, h) in enumerate(sections):
        node = deepcopy(ET.parse(ROOT / 'assets' / (name + '.svg')).getroot())
        prefix = f's{i}-'
        ids = {e.attrib['id']: prefix + e.attrib['id'] for e in node.iter() if 'id' in e.attrib}
        for e in node.iter():
            if e.text == 'Explore the project ↗':
                e.text = 'Project links below ↓'
            elif e.text == '↗' and name.startswith('project-'):
                e.text = '↓'
            if 'id' in e.attrib:
                e.set('id', ids[e.attrib['id']])
            for key, value in list(e.attrib.items()):
                value = re.sub(r'url\(#([^)]*)\)', lambda m: 'url(#' + ids.get(m[1], m[1]) + ')', value)
                if key == 'aria-labelledby':
                    value = ' '.join(ids.get(v, v) for v in value.split())
                e.set(key, value)
        node.attrib.update(x=str(x), y=str(y), width=str(w), height=str(h))
        out.append(node)
    path = ROOT / 'assets' / ('portfolio-mobile.svg' if mobile else 'portfolio.svg')
    ET.ElementTree(out).write(path, encoding='unicode')


if __name__ == '__main__':
    compose()
    compose(mobile=True)
