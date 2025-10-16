import numpy as np
"""
Face Recognition using OpenCV and Haar Cascades
This script performs face detection and recognition on a single image using:
- Haar cascade classifier for face detection
- LBPH (Local Binary Patterns Histograms) face recognizer for identification
The script loads a pre-trained face recognition model and attempts to identify
faces in a test image, displaying the predicted person's name and confidence score.
Dependencies:
    - opencv-python (cv2)
    - numpy
    - Pre-trained model file: 'face_trained.yml'
    - Haar cascade file: '../data/haar_face.xml'
Expected output:
    - Console: Person's name and confidence score
    - Display windows: Original grayscale image and annotated result with bounding boxes
"""
import cv2 as cv

haar_cascade = cv.CascadeClassifier('../data/haar_face.xml')

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('face_trained.yml')

img = cv.imread('../photos/faces/val/elton_john/5.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

faces_react = haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_react:
    faces_roi = gray[y:y+h,x:x+h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    
    print(f'Label - {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0), thickness=2)
    cv.rectangle(img,
                 (x,y),
                 (x+w, y+h),
                 (0,255,0),
                 thickness=2
                 )

cv.imshow('Detected Faces',img)

cv.waitKey(0)