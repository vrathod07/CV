import cv2 as cv 
import numpy as np 


img = cv.imread("assets/landscape.png")

#split the imgage
b,g,r = cv.split(img)

blank = np.zeros(b.shape, dtype="uint8")

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged_img = cv.merge([r,g,b])



while True:
   
    cv.imshow("blue",blue) 
    cv.imshow("green",green) 
    cv.imshow("red",red) 
    cv.imshow("merged image" ,merged_img) 

    
    if(cv.waitKey(1) == ord('q')): 
        break
        

cv.waitKey(0)
cv.destroyAllWindows()