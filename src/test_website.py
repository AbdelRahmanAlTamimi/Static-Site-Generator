import unittest

from website import *

class TestExtractTitle(unittest.TestCase):
    def test_valid_h1_header(self):
        markdown = "# Hello World\nThis is a sample Markdown file."
        expected_title = "Hello World"
        self.assertEqual(extract_title(markdown), expected_title)

    def test_no_h1_header(self):
        markdown = "## Subheader\nThis is a sample Markdown file."
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(
            str(context.exception), "No H1 header found in the Markdown content."
        )



if __name__ == "__main__":
    unittest.main()