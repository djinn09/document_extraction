import unittest
import os
import sys
import cv2
import numpy as np

# Add project root and src to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from preprocessing import preprocess_image
from create_test_image import create_test_image

class TestPreprocessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Generate a test image for the suite."""
        cls.test_image_path = "temp_test_image_for_preprocessing.png"
        create_test_image(output_path=cls.test_image_path)

    @classmethod
    def tearDownClass(cls):
        """Remove the generated test image."""
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)

    def test_preprocess_image_runs(self):
        """Test that the main preprocessing function runs without errors."""
        try:
            result = preprocess_image(self.test_image_path)
            self.assertIsInstance(result, np.ndarray)
        except Exception as e:
            self.fail(f"preprocess_image() raised an exception unexpectedly: {e}")

    def test_preprocess_image_output(self):
        """Test the output of the preprocessing function."""
        result = preprocess_image(self.test_image_path)

        # Should be a numpy array
        self.assertIsInstance(result, np.ndarray)

        # Should be a 2D array (grayscale)
        self.assertEqual(len(result.shape), 2)

        # Should be of type uint8
        self.assertEqual(result.dtype, np.uint8)

        # The values should be either 0 or 255 because of binarization
        self.assertTrue(np.all(np.isin(result, [0, 255])))

if __name__ == '__main__':
    unittest.main()
