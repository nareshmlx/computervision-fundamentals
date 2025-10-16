"""
contours.py
----------------
Demonstrates finding and drawing contours in an image.

Two common approaches to create a binary input for `findContours` are shown:
1) Edge-based: blur -> Canny
2) Thresholding: convert to gray -> threshold

Contours can be useful for shape analysis, object detection and region extraction.
"""

import cv2 as cv
import numpy as np

img = cv.imread("../photos/astinMartin.jpg")
cv.imshow("Original", img)

blank = np.zeros(img.shape, dtype="uint8")

# convert to grayscale for further processing
gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale Image", gray)

# Method 1 : Blur + Canny edges
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edge", canny)

# Method 2 : (alternative) Simple thresholding
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh Image", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) Found !!")

cv.drawContours(blank, contours, -1, (0, 0, 255))
cv.imshow("Contour Image", blank)

cv.waitKey(0)
