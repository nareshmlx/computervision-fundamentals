"""
spaces.py
----------------
Demonstrates conversion between common color spaces with OpenCV (BGR, RGB,
GRAY, HSV, LAB). Use these conversions when performing color-based processing
or visualization.
"""

import cv2 as cv

img = cv.imread("../photos/human.jpg")  ## OPENCV default : BGR !!!!
cv.imshow("Original Image", img)

# plt.imshow(img) ## By Default : RGB
# plt.show()

## ~ BGR to GRAY SCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

## ~ BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

## ~ BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

## ~ BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

## ~ GRAY to BGR (DO not restore colors) splits value across three channels [127,127,127]
bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("Gray to BGR", bgr)

## ~ HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv-->bgr", hsv_bgr)

## ~ HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab-->bgr", lab_bgr)


# plt.imshow(rgb)
# plt.show()
## GRAY SCALE ---> BGR ---> LAB/HSV

cv.waitKey(0)
