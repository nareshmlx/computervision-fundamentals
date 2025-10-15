import cv2 as cv
import numpy as np

img = cv.imread("../photos/human.jpg")

cv.imshow("Human", img)


# ~ Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  
    return cv.warpAffine(img,
                         transMat,
                         dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img,-100,0)
# cv.imshow('Translated',translated)

# ~ Rotation 
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -90)
cv.imshow('Rotated', rotated)

# ~ Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# ~ Flipping
flipped = cv.flip(img, 0)  # 0 for vertical, 1 for horizontal, -1 for both
cv.imshow('Flipped', flipped)

# ~ Cropping
cropped = img[50:200, 200:400]  # y1:y2, x1:x2
cv.imshow('Cropped', cropped)

cv.waitKey(0)
