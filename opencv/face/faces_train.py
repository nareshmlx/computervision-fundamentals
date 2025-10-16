import os
import cv2 as cv
import numpy as np

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]
DIR = "../photos/faces/train"

# p = []
# for i in os.listdir(r'../photos/faces/train'):
#     p.append(i)

# print(p)

features = []
labels = []

haar_cascade = cv.CascadeClassifier('../data/haar_face.xml')

def create_train():
    """
    Creates training data for face recognition by processing images from person directories.
    This function iterates through subdirectories (one per person) in the base directory,
    detects faces in each image using Haar cascade classifier, and extracts face regions
    as training features along with corresponding labels.
    The function populates two global lists:
    - features: Contains grayscale face ROI (Region of Interest) arrays
    - labels: Contains integer labels corresponding to each person (based on index in people list)
    Global variables used:
    - people: List of person names (directory names)
    - DIR: Base directory path containing person subdirectories
    - haar_cascade: Pre-loaded Haar cascade classifier for face detection
    - features: List to store face ROI arrays (modified by this function)
    - labels: List to store corresponding person labels (modified by this function)
    Process:
    1. Iterates through each person directory
    2. Assigns numeric label based on person's index in people list
    3. Processes each image in person's directory
    4. Converts image to grayscale
    5. Detects faces using Haar cascade
    6. Extracts face regions and adds to training data
    Note: This function modifies global features and labels lists directly.
    """
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,
                               cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray,
                                                       scaleFactor=1.1,
                                                       minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Done --------------------')
# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer.create()

face_recognizer.train(features,
                      labels=labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)