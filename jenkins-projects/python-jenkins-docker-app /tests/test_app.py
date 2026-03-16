import unittest
from app import count_errors


class TestLogAnalyzer(unittest.TestCase):

    def test_error_count(self):
        log_data = """
        INFO Server started
        ERROR Connection failed
        INFO Retrying
        ERROR Timeout
        """

        result = count_errors(log_data)

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
