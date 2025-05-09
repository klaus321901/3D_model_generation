import cv2
import matplotlib.pyplot as plt
import numpy as np

def extract_object_from_image(image_path, output_path='processed_image.jpg'):
    """
    Function to extract the object from an image using background subtraction.
    
    Args:
    - image_path (str): The path to the image file.
    - output_path (str): Path where the processed image will be saved.
    
    Returns:
    - Extracted image with background removed.
    """
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return None

    # Convert the image from BGR (OpenCV format) to RGB (for matplotlib display)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert image to grayscale (necessary for background subtraction)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use GaussianBlur to reduce noise before background subtraction
    blurred_image = cv2.GaussianBlur(gray_image, (21, 21), 0)

    # Apply background subtraction: Threshold to isolate the object
    _, thresholded_image = cv2.threshold(blurred_image, 240, 255, cv2.THRESH_BINARY)

    # Perform morphological operations to clean up the thresholded image
    kernel = np.ones((5, 5), np.uint8)
    cleaned_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)

    # Mask the original image to extract only the object (background removed)
    object_extracted = cv2.bitwise_and(image_rgb, image_rgb, mask=cleaned_image)

    # Save the processed image to the output path
    cv2.imwrite(output_path, cv2.cvtColor(object_extracted, cv2.COLOR_RGB2BGR))

    return object_extracted

def load_and_display_image(image_path):
    """
    Function to load and display an image.
    
    Args:
    - image_path (str): The path to the image file.
    """
    # Extract object from image
    object_image = extract_object_from_image(image_path, output_path='processed_image.jpg')

    if object_image is None:
        return

    # Display the extracted object using matplotlib
    plt.imshow(object_image)
    plt.axis('off')  # Hide axis for better visualization
    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\sanat\OneDrive\Desktop\IMG_2304.webp'  # Your image path
    load_and_display_image(image_path)
