"""
smoothing.py
----------------
Demonstrates common blur/smoothing filters in OpenCV:
- Averaging (cv.blur)
- Gaussian (cv.GaussianBlur)
- Median (cv.medianBlur)
- Bilateral (cv.bilateralFilter)

Use these to reduce noise before operations like edge detection or thresholding.
"""

import cv2 as cv

img = cv.imread("../photos/cats.jpg")  # OPENCV default: BGR
cv.imshow("Original", img)

## ~ Averaging (simple mean filter)
average = cv.blur(img, ksize=(3, 3))
cv.imshow("Averaging", average)

## ~ Gaussian Blur (weight decreases with distance from center)
gauss = cv.GaussianBlur(img, (3, 3), sigmaX=0)
cv.imshow("Gaussian Blur", gauss)

## ~ Median Blur (good for salt-and-pepper noise)
median = cv.medianBlur(img, ksize=3)
cv.imshow("Median Blur", median)

## ~ Bilateral Filter (preserves edges while smoothing)
bilateral = cv.bilateralFilter(img, d=10, sigmaColor=50, sigmaSpace=50)
cv.imshow("Bilateral Filter", bilateral)

cv.waitKey(0)
