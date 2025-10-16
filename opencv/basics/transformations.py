"""
transformations.py
----------------
Common geometric image transformations: translation, rotation, resizing,
flipping and cropping. Includes small utility functions `translate` and
`rotate` that can be reused for image processing pipelines.
"""

import cv2 as cv
import numpy as np

img = cv.imread("../photos/human.jpg")
cv.imshow("Human", img)


def translate(img, x, y):
    """
    Translate (shift) an image by (x, y) pixels.

    Args:
        img (numpy.ndarray): source image
        x (int): horizontal shift (positive -> right, negative -> left)
        y (int): vertical shift (positive -> down, negative -> up)

    Returns:
        numpy.ndarray: translated image
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# ~ Rotation
def rotate(img, angle, rotPoint=None):
    """
    Rotate an image around `rotPoint` by `angle` degrees.

    Args:
        img (numpy.ndarray): source image
        angle (float): rotation angle in degrees (positive -> counter-clockwise)
        rotPoint (tuple|None): center of rotation (x, y). If None, image center
                               is used.

    Returns:
        numpy.ndarray: rotated image
    """
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


# examples showing usage of the helpers
translated = translate(img, -100, 0)
rotated = rotate(img, -90)
cv.imshow("Rotated", rotated)

# ~ Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# ~ Flipping
flipped = cv.flip(img, 0)  # 0 for vertical, 1 for horizontal, -1 for both
cv.imshow("Flipped", flipped)

# ~ Cropping
cropped = img[50:200, 200:400]  # y1:y2, x1:x2
cv.imshow("Cropped", cropped)

cv.waitKey(0)
