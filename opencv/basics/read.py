"""
read.py
----------------
Simple examples for reading images and videos with OpenCV.

The video loop shows how to read frames from a file and display them. The
loop includes a safe check for end-of-stream which avoids trying to display
`None` frames when the file finishes.
"""

import cv2 as cv

# Example: read and display a single image
# img  = cv.imread('../photos/astinMartin.jpeg')
# if img is not None:
#     cv.imshow('Astin Martin', img)
#     cv.waitKey(0)

## Reading a video file
capture = cv.VideoCapture("../videos/car.mp4")

while True:
    isTrue, frame = capture.read()
    if not isTrue or frame is None:
        # reached end of file or failed to read the frame
        break

    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
