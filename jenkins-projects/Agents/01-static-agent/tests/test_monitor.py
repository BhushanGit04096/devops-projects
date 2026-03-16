import unittest
from unittest.mock import patch, Mock
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))
from monitor import check_url, load_urls

class TestURLHealthMonitor(unittest.TestCase):

    def test_url_is_up(self):
        mock_response = Mock()
        mock_response.status_code = 200
        with patch('monitor.requests.get', return_value=mock_response):
            result = check_url("https://www.google.com")
            self.assertEqual(result['status'], 'UP')
            self.assertEqual(result['status_code'], 200)

    def test_url_is_down_connection_error(self):
        with patch('monitor.requests.get', side_effect=Exception("Connection Error")):
            result = check_url("https://www.nonexistentwebsite12345.com")
            self.assertEqual(result['status'], 'DOWN')

    def test_load_urls(self):
        test_urls_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'urls.json')
        urls = load_urls(test_urls_path)
        self.assertIsInstance(urls, list)
        self.assertGreater(len(urls), 0)

if __name__ == '__main__':
    unittest.main()
```

---

## What Each Test Does — Plain English
```
test_url_is_up
→ Pretends google.com replied with 200
→ Checks if monitor says UP ✅

test_url_is_down_connection_error
→ Pretends fake URL has no connection
→ Checks if monitor says DOWN ✅

test_load_urls
→ Opens real urls.json
→ Checks if it returns a list with URLs ✅
