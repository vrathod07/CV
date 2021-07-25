import cv2 as cv
import numpy as np

img  = cv.imread("assets/hand.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0,48,80], dtype="uint8")
upper = np.array([20,255,255], dtype="uint8")
skinRegionHSV = cv.inRange(hsv,lower,upper)
blurred = cv.blur(skinRegionHSV,(2,2))
ret, threshold =cv.threshold(blurred,0,255,cv.THRESH_BINARY)

canny = cv.Canny(img, 125,125)

contours, hierarchy = cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countours found')


cv.drawContours(img,contours,-1,(255,0,0),2)



hulll = cv.convexHull(contours[0], returnPoints=False)

defects = cv.convexityDefects(contours[0], hulll)
if (defects != None):
    
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]  
else: 
    print("None") 

while True:
    
    # cv.imshow("image",gray)
    # cv.imshow("Canny",canny)
    cv.imshow("contours",img)
    
    
    if(cv.waitKey(1) == ord('q')): 
        break

cv.waitKey(0)
cv.destroyAllWindows()