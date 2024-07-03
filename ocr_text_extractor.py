import cv2
import pytesseract
import os

def extract_text(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Could not open or find the image.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to get a binary image
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(binary_image)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Optionally, display the processed image
    cv2.imshow('Processed Image', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    if os.path.exists(image_path):
        extract_text(image_path)
    else:
        print("The specified image path does not exist.")
