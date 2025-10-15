import cv2 as cv
import numpy as np

img = cv.imread("../photos/astinMartin.jpg")
cv.imshow("OG Img",img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

gray = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale Image", gray)

## ~ Method 1 : Using Blur and Canny
blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
cv.imshow("Blur Image",blur)

canny = cv.Canny(blur,125,175)
cv.imshow("Canny Edge",canny)

## ~ Method 2 : Using Threshold Funtion
# ret, thresh = cv.threshold(gray, 125, 255,cv.THRESH_BINARY)
# cv.imshow("Thresh Image",thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) Found !!")

cv.drawContours(blank,contours,-1,(0,0,255))
cv.imshow("Contour Image",blank)

cv.waitKey(0)
