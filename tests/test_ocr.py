import unittest
import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Add src directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from ocr import extract_text

class TestOCR(unittest.TestCase):

    def create_dummy_image(self, text):
        """Creates a simple black and white image with the given text."""
        img = Image.new('L', (500, 100), color='white')
        d = ImageDraw.Draw(img)

        # Use a fallback font
        try:
            font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, size=30)
            else:
                font = ImageFont.load_default()
        except IOError:
            font = ImageFont.load_default()

        d.text((10, 10), text, fill='black', font=font)
        # Convert to numpy array, which is what our function expects
        return np.array(img)

    def test_extract_text(self):
        """Test the text extraction function with a clean, simple image."""
        test_text = "Hello OCR"
        dummy_image_array = self.create_dummy_image(test_text)

        extracted_text = extract_text(dummy_image_array)

        # Tesseract can add extra whitespace/newlines, so we strip both strings
        self.assertIn(test_text, extracted_text.strip())

    def test_extract_text_with_empty_image(self):
        """Test that an empty image produces empty text."""
        # Create a blank white image
        empty_image_array = np.full((100, 500), 255, dtype=np.uint8)
        extracted_text = extract_text(empty_image_array)
        self.assertEqual(extracted_text.strip(), "")

    def test_extract_text_easyocr(self):
        """Test the text extraction with the EasyOCR engine."""
        test_text = "Hello EasyOCR"
        dummy_image_array = self.create_dummy_image(test_text)

        # This will download the model on the first run in a test environment
        extracted_text = extract_text(dummy_image_array, engine='easyocr')

        # EasyOCR often returns text line by line, so we check if the text is in the joined output
        self.assertIn(test_text, extracted_text.replace("\n", " "))

    def test_invalid_engine_name(self):
        """Test that an invalid engine name raises a ValueError."""
        # Create a dummy image array
        dummy_image = np.full((100, 500), 255, dtype=np.uint8)
        with self.assertRaises(ValueError):
            extract_text(dummy_image, engine='non_existent_engine')

if __name__ == '__main__':
    unittest.main()
