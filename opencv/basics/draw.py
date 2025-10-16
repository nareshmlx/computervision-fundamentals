"""
draw.py
----------------
Examples of drawing primitives in OpenCV: lines, rectangles, circles and text.

This file shows how to draw shapes onto an image (useful for annotations,
visual debugging and simple graphics overlays). Window titles are descriptive
so you can run the script and inspect each result.
"""

import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")

cv.imshow("Blank", blank)

# # 1. Paint the image a certain color

# blank[0:100,0:100] = 255,0,0 # blank[height,width]
# cv.imshow('Green',blank)

# # 2. Draw a rectangle
# cv.rectangle(blank,(20,20),(blank.shape[1]//2,blank.shape[0]//2),color=(0,255,0),thickness=5)
# cv.rectangle(blank,(20,20),(blank.shape[1]//2,blank.shape[0]//2),color=(0,255,0),thickness=5)
# cv.imshow("Rectangle Drawn",blank)

# # 3. Draw a circle
# cv.circle(blank,
#           center=(blank.shape[1]//2,blank.shape[0]//2),
#           color=(0,0,255),
#           radius=250,
#           thickness=2,
#           )

# cv.imshow("Circle",blank)

# 4. Draw a Line

cv.line(
    blank,
    (250, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    color=(0, 255, 0),
    thickness=5,
)
cv.imshow("Line", blank)

# 5. Put a Text

cv.putText(
    blank, "Hello, OpenCV!", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 255), 1
)
cv.imshow("Text Image", blank)

cv.waitKey(0)
