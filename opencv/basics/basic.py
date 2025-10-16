"""
basic.py
----------------
Collection of small OpenCV examples: reading an image, converting to grayscale,
blurring, edge detection, dilate/erode, resizing and cropping. These snippets
are intended as learning references, not as reusable functions.
"""

import cv2 as cv

img = cv.imread("../photos/human.jpg")
cv.imshow("car", img)
print("BGR IMAGE SHAPE : ", img.shape)
# ## Converting to Gray scale image
gray_img = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("GrayImage", gray_img)
# print("GRAY IMAGE SHAPE : ",gray_img.shape)

## Blurring a image
blur = cv.GaussianBlur(img, ksize=(7, 7), sigmaX=cv.BORDER_DEFAULT)
# cv.imshow("Blurred IMG",blur)

## Edge Cascade
canny = cv.Canny(
    blur,
    threshold1=125,
    threshold2=175,
)
cv.imshow("Edge Img", canny)

## Dilating the image
dilated = cv.dilate(canny, kernel=(3, 3), iterations=3)
# cv.imshow("Dilated Img",dilated)

## Eroding the image
eroded = cv.erode(
    dilated,
    kernel=(
        3,
        3,
    ),
    iterations=3,
)
# cv.imshow("Eroded Img",eroded)

## Resizing the image
resized = cv.resize(img, dsize=(500, 700), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized Img",resized)

## Cropping the image
cropped = img[50:200, 200:400]
# cv.imshow("Cropped Img",cropped)

cv.waitKey(0)
