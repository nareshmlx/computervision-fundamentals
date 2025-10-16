import cv2 as cv
import numpy as np  # noqa: F401

img = cv.imread('../photos/cats.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray,
                                 150,
                                 255,
                                 cv.THRESH_BINARY)
cv.imshow("Simple Thresholded",thresh)

threshold, thresh_inv = cv.threshold(gray,
                                     150,
                                     255,
                                     cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse',thresh_inv)

# Adaptive Thresholding 
adaptive_thresh = cv.adaptiveThreshold(gray,
                                       maxValue=255,
                                       adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       thresholdType=cv.THRESH_BINARY_INV,
                                       blockSize=7,
                                       C=15)

cv.imshow('Adaptive Thresholded',adaptive_thresh)
cv.waitKey(0)