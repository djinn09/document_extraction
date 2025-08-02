import pytesseract
from PIL import Image
import numpy as np

def extract_text(image_array):
    """
    Performs OCR on a preprocessed image array and returns the extracted text.

    :param image_array: A NumPy array representing the preprocessed image.
    :return: A string containing the extracted text.
    """
    if not isinstance(image_array, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    # Convert the NumPy array to a PIL Image
    image = Image.fromarray(image_array)

    # Use Tesseract to extract text
    try:
        text = pytesseract.image_to_string(image)
    except pytesseract.TesseractNotFoundError:
        # This is a common error if Tesseract is not installed or not in the system's PATH
        error_message = (
            "Tesseract is not installed or not in your PATH. "
            "Please install Tesseract and try again.\n"
            "See: https://github.com/tesseract-ocr/tesseract for installation instructions."
        )
        raise RuntimeError(error_message) from None

    return text
