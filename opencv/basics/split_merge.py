import cv2 as cv
import numpy as np

img = cv.imread('../photos/human.jpg') ## OPENCV default : BGR !!!!
cv.imshow('Original Image',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

## ~ Splitting the channels - ~ Shows the Intensity of each channel
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

# cv.imshow('Blue Channel',b)
# cv.imshow('Green Channel',g)
# cv.imshow('Red Channel',r)

cv.imshow('Blue Channel',blue)
cv.imshow('Green Channel',green)
cv.imshow('Red Channel',red)

print(img.shape, b.shape, g.shape, r.shape)

## ~ Merging the channels
merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)



cv.waitKey(0)
