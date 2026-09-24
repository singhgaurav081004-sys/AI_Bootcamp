import cv2
from tkinter import Tk, filedialog

# Open file selection window
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png")
    ]
)

# Read the selected image
image = cv2.imread(file_path)

# Check if image was loaded
if image is None:
    print("Error: Could not open image.")
    exit()

# Resize
resized = cv2.resize(image, (600, 400))

# Crop
cropped = image[50:350, 100:500]

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Increase brightness
bright = cv2.convertScaleAbs(image, alpha=1.2, beta=40)

# Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Edge detection
edges = cv2.Canny(image, 100, 200)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)
cv2.imshow("Cropped Image", cropped)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Brightened Image", bright)
cv2.imshow("Blurred Image", blurred)
cv2.imshow("Edge Detection", edges)

# Save edited images
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("cropped.jpg", cropped)
cv2.imwrite("grayscale.jpg", gray)
cv2.imwrite("brightened.jpg", bright)
cv2.imwrite("blurred.jpg", blurred)
cv2.imwrite("edges.jpg", edges)

print("Image editing completed successfully!")
print("Edited images have been saved.")

cv2.waitKey(0)
cv2.destroyAllWindows()
