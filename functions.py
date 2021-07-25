import cv2 as cv
import numpy as np

img = cv.imread("assets/soccer_practice.jpg")

#turning the image into a grayscale image
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blurring the image
img2 = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)

#Edge cascades: edge detector
canny = cv.Canny(img,125,175)

#dilating the image
dilated = cv.dilate(canny,(7,7),iterations=3)

#eroding
eroded = cv.erode(dilated,(7,7), iterations=3)

#Resize
resize = cv.resize(img,(img.shape[0]//2,img.shape[1]//2))

#cropped image
cropped = img[200:500, 300:400]


while True:

    # cv.imshow("blank",img)
    # cv.imshow("grayscale",img1)
    # cv.imshow("blurred",img2)
    # cv.imshow("edges",canny)
    # cv.imshow("dialted",dilated)
    # cv.imshow("erroded",eroded)
    cv.imshow("resized",resize)
    cv.imshow("cropped",cropped)
    

    if(cv.waitKey(1) == ord('q')): 
        break




cv.waitKey(0)
cv.destroyAllWindows