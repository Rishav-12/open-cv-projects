import cv2

# Load and prepare the image
img = cv2.imread("bookpage.jpeg", 0)
img = cv2.resize(img, (0, 0), fx = 0.7, fy = 0.7)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Apply thresholding to the image
thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 29, 4)

# Display the original image and the resulting image
cv2.imshow("Image", img)
cv2.imshow("Result", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
