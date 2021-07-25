import cv2
import numpy as np
 
cap = cv2.VideoCapture(0) #it will take hold of the camera 

while True: 
    
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    #image = np.zeros(frame.shape, np.uint8)
    # smaller_image = cv2.resize(frame,(0,0), fx=0.5, fy =0.5)
    
    # image[:height//2,:width//2] = smaller_image
    # image[height//2:,:width//2] = smaller_image
    # image[:height//2,width//2:] = cv2.rotate(smaller_image, cv2.cv2.ROTATE_180)
    # image[height//2:,width//2:] = smaller_image
    
    #to draw a line on the image
    # img = cv2.line(frame,(0,0), (width,height), (255,0,0),10)
    # img = cv2.line(img,(width,0), (0,height), (255,0,0),10)
    
    # img = cv2.rectangle(frame,(0,0),(width//2,height//2),(0,255,0),5)
    
    # img = cv2.circle(frame,(width//2,height//2),width//2,(0,0,0),3)
    
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # img  = cv2.putText(frame,"I'm the best", (200,height - 50),font,1, (0,0,0), 2)
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   
    lower_blue = np.array([0, 70, 50])
    upper_blue = np.array([10, 255, 255])
    lower_blue_1 = np.array([170, 70, 50])
    upper_blue_1 = np.array([180, 255, 255])
    
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    mask1 = cv2.inRange(hsv,lower_blue_1,upper_blue_1)
    
    result = cv2.bitwise_and(frame,frame,mask)
    cv2.imshow("mask", result)
    cv2.imshow('frame',mask) #show the frame
    
    if (cv2.waitKey(1) == ord('q')):  # if the key pressed is q quit the windows
        break

cap.release()
cv2.destroyAllWindows()