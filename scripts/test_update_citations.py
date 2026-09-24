import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import update_citations as updater


def table(values):
    return '<table id="gsc_rsb_st"><tbody><tr>' + ''.join(
        '<td class="gsc_rsb_std">' + value + '</td>' for value in values
    ) + '</tr></tbody></table>'


class CitationTests(unittest.TestCase):
    def test_all_time_not_recent_or_article_citations(self):
        html = '<td class="gsc_rsb_std">999</td>' + table(['1,550', '1549', '19', '19', '31', '31'])
        self.assertEqual(updater.parse_citations(html), 1550)

    def test_zero_is_a_valid_count(self):
        self.assertEqual(updater.parse_citations(table(['0'] * 6)), 0)

    def test_block_and_invalid_values_are_rejected(self):
        for html in ['<h1>Unusual traffic</h1>', table(['-'] * 6), table(['12'])]:
            with self.assertRaises(ValueError):
                updater.parse_citations(html)

    def test_failed_fetch_never_saves(self):
        with patch.object(updater, 'fetch_citations', side_effect=ValueError('blocked')), patch.object(updater, 'save_citations') as save:
            with self.assertRaises(ValueError):
                updater.main()
            save.assert_not_called()

    def test_json_and_html_fallback_agree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'index.html').write_text('<strong id="scholar-citation-count" aria-live="polite">1,446</strong>')
            updater.save_citations(root, 'HdXMhfcAAAAJ', 1550)
            data = json.loads((root / 'citation-data.json').read_text())
            self.assertEqual(data['citations'], 1550)
            self.assertIsNotNone(data['updated_at'])
            self.assertIn('>1,550</strong>', (root / 'index.html').read_text())

    def test_changed_counter_does_not_overwrite_json(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'index.html').write_text('<html></html>')
            (root / 'citation-data.json').write_text('previous data')
            with self.assertRaises(ValueError):
                updater.save_citations(root, 'HdXMhfcAAAAJ', 1550)
            self.assertEqual((root / 'citation-data.json').read_text(), 'previous data')


if __name__ == '__main__':
    unittest.main()
