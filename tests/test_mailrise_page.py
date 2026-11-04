"""Publication contracts for the Mailrise static landing page (standard library only)."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.nodes = []
        self.text = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.nodes.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class MailrisePageAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = (ROOT / 'mailrise/index.html').read_text()
        cls.doc = Document(cls.source)
        cls.words = ' '.join(cls.doc.text)

    def test_english_accessible_document(self):
        html = [attrs for tag, attrs in self.doc.nodes if tag == 'html']
        self.assertEqual(len(html), 1)
        self.assertEqual(html[0].get('lang'), 'en')
        for tag in ('main', 'h1', 'title'):
            self.assertEqual(sum(t == tag for t, _ in self.doc.nodes), 1, tag)
        self.assertFalse(re.search(r'[가-힣]', self.words))

    def test_core_product_and_requirements_are_explained(self):
        for phrase in ('Mailrise', 'Gmail', 'iPhone', 'iPad', 'Today', 'Upcoming',
                       'Pick', 'Keep', 'Complete', 'Apple Intelligence'):
            self.assertIn(phrase, self.words)
        self.assertRegex(self.words, r'(?:iOS|iPadOS)\s*26')
        self.assertRegex(self.words.lower(), r'on.device')

    def test_discovery_metadata(self):
        metas = {a.get('name', a.get('property')): a.get('content', '')
                 for t, a in self.doc.nodes if t == 'meta'}
        self.assertTrue(metas.get('description'))
        self.assertIn('width=device-width', metas.get('viewport', ''))
        self.assertTrue(metas.get('og:title'))
        self.assertTrue(metas.get('og:description'))
        canonical = [a.get('href') for t, a in self.doc.nodes
                     if t == 'link' and a.get('rel') == 'canonical']
        self.assertEqual(canonical, ['https://windystudio.com/mailrise/'])

    def test_links_and_assets_resolve(self):
        ids = [a['id'] for _, a in self.doc.nodes if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)), 'duplicate fragment targets')
        for tag, attrs in self.doc.nodes:
            for attribute in ('href', 'src'):
                if attribute not in attrs:
                    continue
                url = attrs[attribute]
                self.assertNotIn(url, ('', '#'), 'placeholder link')
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc:
                    self.assertNotIn(parsed.scheme, ('javascript', 'data'))
                    continue
                if parsed.path:
                    path = (ROOT / unquote(parsed.path.lstrip('/')) if parsed.path.startswith('/')
                            else ROOT / 'mailrise' / unquote(parsed.path))
                    self.assertTrue(path.exists(), url)
                if parsed.fragment and not parsed.path:
                    self.assertIn(parsed.fragment, ids)

    def test_images_have_alternatives(self):
        images = [a for t, a in self.doc.nodes if t == 'img']
        self.assertTrue(images, 'use the real Mailrise brand asset')
        for attrs in images:
            self.assertIn('alt', attrs)

    def test_illustrative_content_is_labelled(self):
        self.assertRegex(self.words.lower(), r'(illustrative|sample|example)')

    def test_no_unverified_download_or_placeholder_claims(self):
        self.assertNotRegex(self.source.lower(), r'apps\.apple\.com|testflight\.apple\.com|lorem ipsum')


if __name__ == '__main__':
    unittest.main()
