"""
bitwise.py
----------------
Demonstrates bitwise operations on simple shapes using OpenCV.

This tutorial shows:
- creating simple binary shapes (rectangle, circle)
- computing bitwise AND / OR / XOR / NOT

These operations are useful when combining or manipulating masks and regions
of interest.
"""

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")

# create two filled shapes
rectangle = cv.rectangle(
    blank.copy(), (30, 30), (370, 370), (255, 255, 255), thickness=-1
)
circle = cv.circle(
    blank.copy(), center=(200, 200), radius=200, color=(255, 255, 255), thickness=-1
)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise AND -> pixels present in both shapes (intersection)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# bitwise OR -> pixels present in either shape (union)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# bitwise NOT -> invert pixels (useful for masks)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT", bitwise_not)

# XOR -> pixels in one shape or the other but not both
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

cv.waitKey(0)
