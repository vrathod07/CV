import numpy as np
import cv2 

img1 = cv2.imread("assets/Chess_Board1.png")
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

N = 100
corners = cv2.goodFeaturesToTrack(img,N,0.2,10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img1,(x,y),5,(255,0,0),-1)

for i in range(len(corners)): 
    for j in range(len(corners)): 
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        #color = np.random.randint(0,255,size=3)
        cv2.line(img1,corner1,corner2,(0,0,0),1)

cv2.imshow("frame",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()