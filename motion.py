import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

subtractor = cv.createBackgroundSubtractorMOG2(20,50)


  
while True:                      
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    if ret: 
        mask = subtractor.apply(frame)
        cv.imshow('mask',mask) #show the frame
    else:
        cap = cv.VideoCapture(0)
        
    if (cv.waitKey(1) == ord('q')):  # if the key pressed is q quit the windows
        break

cap.release()
cv.destroyAllWindows()