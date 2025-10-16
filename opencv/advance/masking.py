"""
masking.py
----------------
Small examples of creating binary masks (circle, rectangle), combining them
and applying the resulting mask to an image using `cv.bitwise_and`.

This is a tutorial-style script; it demonstrates core masking concepts used in
many computer vision tasks (region-of-interest extraction, selective filtering,
etc.).
"""

import cv2 as cv
import numpy as np

img = cv.imread("../photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Img", blank)

# create a circular mask centered in the image
circle_mask = cv.circle(
    blank.copy(),
    (img.shape[1] // 2, img.shape[0] // 2),  # (w,h)
    100,
    255,
    -1,
)

# create a rectangular mask
rectangle_mask = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# combine masks using bitwise AND (intersection)
weird_mask = cv.bitwise_and(circle_mask, rectangle_mask)
print(blank.shape)
cv.imshow("Mask", weird_mask)

# apply mask to image (keeps pixels where mask != 0)
masked = cv.bitwise_and(img, img, mask=weird_mask)
cv.imshow("Masked", masked)

cv.waitKey(0)
