"""
histogram.py
----------------
Small demo showing how to compute and plot color histograms in OpenCV.

This script demonstrates:
- creating a binary mask
- computing per-channel color histograms with `cv.calcHist`
- plotting results with matplotlib

Usage:
    Run as a script for interactive viewing (displays windows with images and plots).

Notes:
    This file is intended as a tutorial example. It reads a sample image from
    ../photos/cats.jpg relative to the repository and shows a masked color
    histogram. It does not expose functions for import; if you want to reuse
    functionality programmatically, wrap the plotting code in functions.
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Mask", masked)

##  Grayscale histogram
# gray_hist = cv.calcHist(images=[gray],
#                         channels=[0],
#                         mask=mask,
#                         histSize=[256],
#                         ranges=[0,256])

# gray_hist = cv.calcHist

# plt.figure()
# plt.title("GrayScale Histogram")
# plt.xlabel("Bin")
# plt.ylabel("No of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# ~ ----------------------------------------
## Color Histogram
colors = ("b", "g", "r")

plt.figure()
plt.title("COlor Histogram")
plt.xlabel("Bin")
plt.ylabel("No of Pixels")

for i, col in enumerate(colors):
    # compute histogram for each channel separately
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
cv.waitKey(0)
