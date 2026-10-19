from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FILES = ['readme-hero', 'clipdeck-banner', 'project-whisper', 'project-aetherdb',
         'project-argus', 'project-syskit', 'engineering-approach', 'contact-console']
FILES += [name + '-mobile' for name in ['readme-hero', 'clipdeck-banner', 'engineering-approach', 'contact-console']]
FILES += ['portfolio', 'portfolio-mobile']


class PortfolioTests(unittest.TestCase):
    def test_self_contained_accessible_assets(self):
        for name in FILES:
            with self.subTest(name=name):
                p = ROOT / 'assets' / (name + '.svg')
                self.assertTrue(p.exists())
                svg = ET.parse(p).getroot()
                tags = [e.tag.split('}')[-1] for e in svg.iter()]
                self.assertIn('title', tags)
                self.assertIn('desc', tags)
                self.assertNotIn('script', tags)
                self.assertNotIn('image', tags)
                for e in svg.iter():
                    for k, v in e.attrib.items():
                        if k.endswith('href'):
                            self.assertTrue(v.startswith('#'))
                self.assertIn('prefers-reduced-motion', p.read_text())

    def test_approved_copy(self):
        hero = (ROOT / 'assets/readme-hero.svg').read_text()
        self.assertIn('Software developer', hero)
        self.assertIn('I like building useful software.', hero)
        feature = (ROOT / 'assets/clipdeck-banner.svg').read_text()
        self.assertIn('conceptual CLI illustration', feature)
        self.assertNotIn('base64', feature)
        self.assertNotIn('v0.', feature)
        self.assertIn('Have something in mind?', (ROOT / 'assets/contact-console.svg').read_text())

    def test_readme_destinations_and_sections(self):
        readme = (ROOT / 'README.md').read_text()
        for repo in ['clipdeck', 'WhisperSocial-Backend', 'AetherDB', 'Argus', 'syskit']:
            self.assertIn('https://github.com/Mersad-Moghaddam/' + repo, readme)
        self.assertIn('mailto:nickmersad81@gmail.com', readme)
        self.assertIn('linkedin.com/in/mersad-moghaddam', readme)
        self.assertIn('x.com/MersadMoghadam', readme)
        self.assertIn('portfolio.svg', readme)
        for old in ['github-signal.svg', 'incident-replay.svg', 'toolkit-rack.svg']:
            self.assertNotIn(old, readme)
        for src in re.findall(r'src="(\./[^"]+)"', readme):
            self.assertTrue((ROOT / src).exists())

    def test_mobile_layout_sources(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertEqual(readme.count('<picture>'), 1)
        self.assertIn('media="(max-width: 600px)"', readme)
        self.assertNotIn('width="49%"', readme)
        for src in re.findall(r'srcset="(\./[^"]+)"', readme):
            self.assertTrue((ROOT / src).exists())

    def test_single_continuous_canvas(self):
        readme = (ROOT / 'README.md').read_text()
        self.assertEqual(len(re.findall(r'<img\b', readme)), 1)
        for name in ['portfolio', 'portfolio-mobile']:
            p = ROOT / 'assets' / (name + '.svg')
            self.assertTrue(p.exists())
            svg = ET.parse(p).getroot()
            ids = [e.attrib['id'] for e in svg.iter() if 'id' in e.attrib]
            self.assertEqual(len(ids), len(set(ids)))
            for title in ['ClipDeck', 'Whisper Social', 'AetherDB', 'Argus', 'SysKit', 'How I work']:
                self.assertIn(title, p.read_text())


if __name__ == '__main__':
    unittest.main()
