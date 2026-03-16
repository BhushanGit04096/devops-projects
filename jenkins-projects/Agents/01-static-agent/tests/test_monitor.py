import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from monitor import load_urls

class TestURLHealthMonitor(unittest.TestCase):

    def test_load_urls(self):
        # Opens real urls.json
        # Checks if it returns a list with URLs
        test_urls_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'urls.json')
        urls = load_urls(test_urls_path)
        self.assertIsInstance(urls, list)
        self.assertGreater(len(urls), 0)

    def test_urls_not_empty(self):
        # Checks each URL is a non empty string
        test_urls_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'urls.json')
        urls = load_urls(test_urls_path)
        for url in urls:
            self.assertTrue(len(url) > 0)

if __name__ == '__main__':
    unittest.main()
