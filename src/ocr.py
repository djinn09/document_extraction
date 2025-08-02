import pytesseract
from PIL import Image
import numpy as np
import easyocr

def _run_tesseract(image_array):
    """
    Performs OCR using Tesseract.
    """
    if not isinstance(image_array, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    image = Image.fromarray(image_array)

    try:
        text = pytesseract.image_to_string(image)
    except pytesseract.TesseractNotFoundError:
        error_message = (
            "Tesseract is not installed or not in your PATH. "
            "Please install Tesseract and try again."
        )
        raise RuntimeError(error_message) from None

    return text

def _run_easyocr(image_array):
    """
    Performs OCR using EasyOCR.
    """
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_array)
    text_list = [text for _, text, _ in result]
    return "\n".join(text_list)

# A dictionary to map engine names to their functions
OCR_ENGINES = {
    'tesseract': _run_tesseract,
    'easyocr': _run_easyocr,
}

def extract_text(image_array, engine='tesseract'):
    """
    Performs OCR on a preprocessed image array using the specified engine.

    :param image_array: A NumPy array representing the preprocessed image.
    :param engine: A string specifying the OCR engine to use.
    :return: A string containing the extracted text.
    """
    if engine not in OCR_ENGINES:
        raise ValueError(f"Unknown OCR engine: {engine}. Available engines are: {list(OCR_ENGINES.keys())}")

    engine_function = OCR_ENGINES[engine]

    return engine_function(image_array)
