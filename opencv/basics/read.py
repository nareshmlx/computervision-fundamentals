import cv2 as cv 

# img  = cv.imread('../photos//astinMartin.jpeg')

# cv.imshow('Astin Martin', img)

# cv.waitKey(0) # 0 means wait indefinitely until a key is pressed

## Reading a video file
capture = cv.VideoCapture('../videos/car.mp4')

while True:
    isTrue, frame = capture.read() 
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()   
cv.destroyAllWindows()


