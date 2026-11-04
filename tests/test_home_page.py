"""Visitor-facing contracts for the redesigned studio home (stdlib only)."""
import re
import os
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = Path(os.environ.get('SITE_ROOT', str(ROOT / '_site')))


class HomeDocument(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.nodes, self.text, self.headings = [], [], []
        self.heading = None
        self.links, self.active_link = [], None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))
        if tag == 'a':
            self.active_link = {'attrs': dict(attrs), 'text': '', 'images': []}
            self.links.append(self.active_link)
        if tag == 'img' and self.active_link is not None:
            self.active_link['images'].append(dict(attrs))
        if re.fullmatch(r'h[1-6]', tag):
            self.heading = ''

    def handle_data(self, data):
        self.text.append(data)
        if self.active_link is not None:
            self.active_link['text'] += data
        if self.heading is not None:
            self.heading += data

    def handle_endtag(self, tag):
        if tag == 'a':
            self.active_link = None
        if re.fullmatch(r'h[1-6]', tag) and self.heading is not None:
            self.headings.append(self.heading.strip())
            self.heading = None


class HomePageAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (SITE_ROOT / 'index.html').read_text()
        cls.doc = HomeDocument(cls.source)
        cls.words = ' '.join(' '.join(cls.doc.text).split())

    def test_studio_identity_and_purpose(self):
        self.assertIn('windystudio™', self.words)
        self.assertRegex(self.words, r'온디바이스\s*AI|[Oo]n-device\s*AI')
        self.assertRegex(self.words, r'연구|[Rr]esearch')
        self.assertRegex(self.words, r'개발|[Dd]evelop')
        self.assertNotIn('View on GitHub', self.words)
        self.assertNotIn('winDy and 21st Century Radio Band (windystudio.com)', self.words)

    def test_preserves_existing_names_and_descriptions(self):
        phrases = [
            'winDy = win of indie', '아이작 아시모프처럼 명쾌하게 생각하기',
            '마셜 로젠버그처럼 대화하기', '스콧 니어링처럼 죽기',
            '21st Century Radio Band (21세기라디오밴드)', 'Member', 'Guest', 'LIVE',
            'winDy: Vocal, Guitar', '영근: Vocal, Percussion',
            '병윤: Bass', '준식: Vocal, Guitar, Bass',
            '2018년 5월 1일 (우아한 푸줏간 이태원동 118-4 / 7시 30분)',
            'programming', 'blockchain', 'coding tools', 'using computer',
            'Boardgame', 'Assemble the Army (TCG)', 'Mailrise',
            'A clearer inbox. A lighter day.',
            'Important Gmail messages, dates, and on-device AI summaries for iPhone and iPad.'
        ]
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.words)

    def test_mailrise_is_before_windy(self):
        headings = self.doc.headings
        self.assertIn('winDy', headings)
        self.assertIn('Mailrise', headings)
        self.assertLess(headings.index('Mailrise'), headings.index('winDy'))

    def test_intro_and_footer_are_english(self):
        self.assertIn('windystudio™ is a development group researching and building a range of applications powered by on-device AI.', self.words)
        footer = re.search(r'<footer\b[^>]*>(.*?)</footer>', self.source, re.S)
        self.assertIsNotNone(footer)
        words = ' '.join(' '.join(HomeDocument(footer.group(1)).text).split())
        self.assertIn('On-device AI application research and development', words)
        self.assertIn('Built with Jekyll and the Minima theme.', words)
        self.assertNotRegex(words, r'[가-힣]')

    def test_mailrise_title_and_icon_are_links(self):
        section = re.search(r'<section\b[^>]*id="mailrise"[^>]*>(.*?)</section>', self.source, re.S)
        self.assertIsNotNone(section)
        links = HomeDocument(section.group(1)).links
        self.assertTrue(any(link['text'].strip() == 'Mailrise'
                            and link['attrs'].get('href') == '/mailrise/' for link in links))
        self.assertTrue(any(link['attrs'].get('href') == '/mailrise/'
                            and any(img.get('src') == '/mailrise/assets/app-icon.png'
                                    for img in link['images']) for link in links))

    def test_existing_destinations_are_preserved(self):
        links = [urlsplit(a['href']).path for t, a in self.doc.nodes if t == 'a' and 'href' in a]
        for path in ['/programming/', '/boardgame/', '/mailrise/',
                     '/21stCenturyRadioBand/live_20180501.html']:
            self.assertIn(path, links)

    def test_accessible_document_and_original_logo(self):
        self.assertEqual(sum(t == 'h1' for t, _ in self.doc.nodes), 1)
        self.assertEqual(sum(t == 'main' for t, _ in self.doc.nodes), 1)
        self.assertTrue(any(t == 'html' and a.get('lang') for t, a in self.doc.nodes))
        images = [a for t, a in self.doc.nodes if t == 'img']
        self.assertTrue(any(a.get('src') == '/assets/images/windystudio.png' for a in images))
        for attrs in images:
            self.assertIn('alt', attrs)

    def test_metadata_and_local_assets(self):
        meta = {a.get('name', a.get('property')): a.get('content', '')
                for t, a in self.doc.nodes if t == 'meta'}
        self.assertTrue(meta.get('description'))
        self.assertIn('width=device-width', meta.get('viewport', ''))
        self.assertEqual(meta.get('og:site_name'), 'windystudio™')
        self.assertIn(('link', {'rel': 'canonical', 'href': 'https://windystudio.com/'}), self.doc.nodes)
        ids = [a['id'] for _, a in self.doc.nodes if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        for tag, attrs in self.doc.nodes:
            if tag == 'a':
                href = attrs.get('href', '')
                self.assertNotIn(href, ('', '#'))
                if href.startswith('#'):
                    self.assertIn(href[1:], ids)
            if tag == 'img' or (tag == 'link' and attrs.get('rel') in ('stylesheet', 'icon')):
                url = attrs.get('src', attrs.get('href', ''))
                parts = urlsplit(url)
                self.assertFalse(parts.scheme or parts.netloc, 'assets must be local')
                self.assertTrue((SITE_ROOT / unquote(parts.path.lstrip('/'))).is_file(), url)

    def test_rendered_with_jekyll(self):
        self.assertTrue(any(t == 'meta' and a.get('name') == 'generator'
                            and a.get('content', '').startswith('Jekyll')
                            for t, a in self.doc.nodes))
        self.assertNotIn('{%', self.source)
        self.assertNotIn('{{', self.source)


if __name__ == '__main__':
    unittest.main()
