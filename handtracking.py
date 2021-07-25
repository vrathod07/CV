import cv2
import mediapipe as mp 
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True: 
    
    success, image = cap.read()
    cv2.imshow("image",image)
    
    imagRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imagRGB)
    print(results.multi_hand_landmarks)

    if(cv2.waitKey(1) == ord('q')): 
        break
    
cv2.waitKey(0)
cv2.destroyAllWindows()