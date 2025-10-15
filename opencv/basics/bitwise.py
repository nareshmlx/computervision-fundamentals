import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),(255,255,255),thickness=-1)
circle = cv.circle(blank.copy(),center=(200,200),radius=200,color=(255,255,255),thickness=-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Blank",circle)

# bitwise AND 
bitwise_and = cv.bitwise_and(rectangle, circle) # Intersecting Region
cv.imshow("Bitwise AND", bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle) # Both Intersecting and non intersecting regions
cv.imshow("Bitwise OR", bitwise_or)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle) # Inverting 1 -> 0 : 0 -> 1
cv.imshow("Bitwise NOT", bitwise_not)

# # bitwise XOR
# bitwise_xor = cv.bitwise_xor(rectangle, circle) # Non-Intersecting Region
# cv.imshow("Bitwise XOR", bitwise_xor)

bitwise_xor = bitwise_or - bitwise_and
cv.imshow("Bitwise XOR",bitwise_xor)

cv.waitKey(0)