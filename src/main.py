import argparse
from preprocessing import preprocess_image
from ocr import extract_text
from postprocessing import postprocess_text
import cv2

def main():
    """
    Main function to run the OCR pipeline.
    """
    parser = argparse.ArgumentParser(description="A simple OCR pipeline.")
    parser.add_argument("image_path", help="The path to the image to process.")
    args = parser.parse_args()

    try:
        # Step 1: Preprocess the image
        print("Step 1: Preprocessing image...")
        preprocessed_image = preprocess_image(args.image_path)
        # For debugging, you might want to save the preprocessed image
        # cv2.imwrite("preprocessed_image.png", preprocessed_image)
        print("Preprocessing complete.")

        # Step 2: Extract text using OCR
        print("\nStep 2: Extracting text...")
        raw_text = extract_text(preprocessed_image)
        print("Text extraction complete.")
        print("--- Raw Text ---")
        print(raw_text)
        print("------------------")

        # Step 3: Post-process the text
        print("\nStep 3: Post-processing text...")
        final_text = postprocess_text(raw_text)
        print("Post-processing complete.")

        # Final Output
        print("\n--- Final Processed Text ---")
        print(final_text)
        print("----------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{args.image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
