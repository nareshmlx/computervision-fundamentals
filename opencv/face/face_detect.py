import cv2 as cv
"""
Face detection script using OpenCV and Haar Cascade Classifier.
This script loads an image, converts it to grayscale, and uses a pre-trained
Haar cascade classifier to detect faces in the image. Detected faces are
highlighted with green rectangles and displayed in a window.
Requirements:
    - OpenCV (cv2)
    - Haar cascade XML file for face detection
    - Input image file
Input Files:
    - '../photos/group2.jpg': Source image containing faces to detect
    - '../data/haar_face.xml': Pre-trained Haar cascade classifier for face detection
Output:
    - Displays original image with detected faces marked by green rectangles
    - Prints the total number of faces detected to console
    - Shows intermediate grayscale conversion for processing
Parameters used for face detection:
    - scaleFactor: 1.1 (image pyramid scaling factor)
    - minNeighbors: 3 (minimum number of neighbor rectangles for detection)
Note: Press any key to close the display windows.
"""

img = cv.imread('../photos/group2.jpg')
cv.imshow('Group',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('../data/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray,
                                           scaleFactor=1.1,
                                           minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h), (0,255,0), thickness=2)
    
cv.imshow("Detected Faces",img)

cv.waitKey(0)