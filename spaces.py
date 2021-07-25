import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("assets/landscape.png")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#hsv to bgr
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)



while True:
    
    # cv.imshow("landscape",img)
    # cv.imshow("landscape",gray)
    #cv.imshow("landscape",rgb)
    # plt.imshow(img)
    # plt.show()
    cv.imshow("landscape",hsv_bgr)
    
    if(cv.waitKey(1) == ord('q')): 
        break

cv.waitKey(0)
cv.destroyAllWindows()