import cv2 
import numpy as np

PATH = "assets/images/moana.jpg"

o_img = cv2.imread(PATH)

img = cv2.cvtColor(o_img,cv2.COLOR_BGR2GRAY)

blank_image = np.zeros(img.shape)


#Simple thresholding
#1. BINARY thresholding
(T,binary) = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#2.INV  BINARY thresholding
(T1, inv_binary) = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

#3. TRUNC thresholding
(T2, trunc) = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

#1. TO ZERO thresholding
(T3,to_zero) = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

#1.  TO ZERO INV thresholding
(T4, to_zero_inv) = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)



"""Adaptive Thresholding"""

#1. Mean Adaptive Thresholding
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

#1. Guassian Adaptive Thresholding
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

# Otsu's thresholding
ret2,th_otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

while True:

    cv2.imshow("original image",o_img)
    cv2.imshow("grayscale image",img)
    cv2.imshow("binary threshold image",binary)
    cv2.imshow("inverse binary threshold image",inv_binary)
    cv2.imshow("trunc image",trunc)
    cv2.imshow("to zero image",to_zero)
    cv2.imshow("to zero inv image",to_zero_inv)
    cv2.imshow("adaptive mean threshold image",th2)
    cv2.imshow("adaptive guassian threshold image",th3)
    cv2.imshow("otsu threshold image",th_otsu)

    if(cv2.waitKey(1) == ord('q')): 
        break
