import cv2 as cv

img = cv.imread('../photos/cats.jpg')  # OPENCV default: BGR
cv.imshow("Human",img)

## ~ Averaging

average = cv.blur(img,
                  ksize=(3,3))
cv.imshow('Averaging',average)

## ~ Gaussian Blur
gauss = cv.GaussianBlur(img,(3,3),
                        sigmaX=0)
cv.imshow('Gaussian Blur', gauss)

## ~ Median Blur
median = cv.medianBlur(img, ksize=3)
cv.imshow('Median Blur', median)

## ~ Bilateral Filter
bilateral = cv.bilateralFilter(img, d=10, sigmaColor=50, sigmaSpace=50)
cv.imshow('Bilateral Filter', bilateral)

cv.waitKey(0)