import numpy as np 
import cv2 as cv #

img  =  cv.imread("assets/louis.png")

#translation
def translate(img,x,y): 
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(img,100,100)

#rotation
def rotate(img,angle,rotatePoint=None):
    
    (height,width) = img.shape[:2]
    
    if rotatePoint is None:
        rotatePoint =(width//2,height//2) 
    rotateMatrix = cv.getRotationMatrix2D(rotatePoint, angle,1.0)
    dimensions = (width,height)
    
    return cv.warpAffine(img,rotateMatrix,dimensions)

rotation = rotate(img,90)

#Resize image
resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
        
#Flipping
flip = cv.flip(resize,2)

#cropping
cropped = resize[200:300, 300:400]


while True: 
    
    
    cv.imshow("image",cropped)
    
    if(cv.waitKey(1) == ord('q')): 
        break
cv.waitKey(0)
cv.destroyAllWindows()