import unittest
import sys
import os

# Add src directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from postprocessing import correct_spelling, adjust_format, postprocess_text

class TestPostprocessing(unittest.TestCase):

    def test_correct_spelling(self):
        """Test the spelling correction function."""
        text = "This is a test with some misteaks."
        corrected_text = correct_spelling(text)
        self.assertIn("mistakes", corrected_text)
        self.assertNotIn("misteaks", corrected_text)

    def test_adjust_format(self):
        """Test the format adjustment function."""
        text = "  This has   extra spaces. \n\n And multiple newlines.  "
        formatted_text = adjust_format(text)
        self.assertEqual(formatted_text, "This has extra spaces.\nAnd multiple newlines.")

    def test_postprocess_text(self):
        """Test the full post-processing pipeline."""
        text = "  This is a tset with some misteaks. \n\n"
        processed_text = postprocess_text(text)
        # It should correct 'tset' to 'test' and 'misteaks' to 'mistakes' and fix formatting
        self.assertEqual(processed_text, "This is a test with some mistakes.")

if __name__ == '__main__':
    unittest.main()
