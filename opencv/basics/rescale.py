import cv2 as cv



def rescaleFrame(frame,scale=0.75):
    """
    Works for images,videos and live video
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,
                     dsize=dimensions,
                     interpolation=cv.INTER_AREA)
    
img = cv.imread('../photos/astinMartin.jpeg')
rescaled_img = rescaleFrame(img, 0.2)
cv.imshow('Astin Martin', rescaled_img)
cv.imwrite('../photos/car_rescaled.jpeg', rescaled_img)
cv.waitKey(0)
## VIdeo setting 

def changeRes(width,height):
    """
    Only for live video
    """
    capture.set(3,width)
    capture.set(4,height)
    
## Video Capture
capture = cv.VideoCapture('../videos/car.mp4')

while True:
    isTrue, frame = capture.read() 
    
    rescaled_frame = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', rescaled_frame)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()   
cv.destroyAllWindows()
