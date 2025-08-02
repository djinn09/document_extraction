import cv2
import numpy as np

def noise_reduction(image):
    """Applies noise reduction to a grayscale image using a median filter."""
    # The kernel size (e.g., 3 or 5) must be an odd number.
    return cv2.medianBlur(image, 3)

def deskew(image):
    """Corrects the skew of a grayscale image."""
    # Invert the image
    gray = cv2.bitwise_not(image)

    # Threshold the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Find contours
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # Rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    return rotated

def binarize(image):
    """Converts a grayscale image to binary using adaptive thresholding."""
    return cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

def segment(image):
    """Placeholder for a segmentation function."""
    # Pytesseract has its own page segmentation, so this might not be needed
    # for a simple pipeline.
    return image

def preprocess_image(image_path):
    """
    Runs the full preprocessing pipeline on an image.
    Returns a preprocessed image ready for OCR.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image at path '{image_path}' not found or could not be read.")

    # The order of operations can matter.
    # 1. Deskew
    deskewed = deskew(img)

    # 2. Noise Reduction
    denoised = noise_reduction(deskewed)

    # 3. Binarization
    binary = binarize(denoised)

    # 4. Segmentation (placeholder)
    final_img = segment(binary)

    return final_img
