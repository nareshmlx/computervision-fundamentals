import cv2 as cv
import numpy as np 

img = cv.imread('../photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Img',blank)

circle_mask = cv.circle(blank.copy(),
                 (img.shape[1]//2,img.shape[0]//2), # (w,h)
                 100,
                 255,
                 -1)

rectangle_mask = cv.rectangle(blank.copy(),
                         (30,30),
                         (370,370),
                         255,
                         -1)

weird_mask = cv.bitwise_and(circle_mask,rectangle_mask)
print(blank.shape)
cv.imshow('Mask',weird_mask)

masked = cv.bitwise_and(img,img,mask=weird_mask)
cv.imshow('Masked',masked)

cv.waitKey(0)


