import cv2 as cv 
import numpy as np 


img = cv.imread("assets/landscape.png")

while True:
   
 
    if(cv.waitKey(1) == ord('q')): 
        break
        

cv.waitKey(0)
cv.destroyAllWindows()