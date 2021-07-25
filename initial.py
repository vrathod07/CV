import cv2
import random

#load the image
img = cv2.imread('assets/screen-2.jpg',-1)

# #resize the Image
# #img_2 = cv2.resize(img,(400,400)) #resize in terms of pixels
# img_2 = cv2.resize(img,(0,0), fx=0.5,fy=0.5) #resize in terms of height and width

# #rotate the image
# img_3 = cv2.rotate(img,cv2.cv2.ROTATE_180)

# #write the image to new folder
# cv2.imwrite('assets/new_image.jpg',img)

# #display the image
# cv2.imshow('Image',img_3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


### Image Manipulation

#print the shape
# print(img.shape)
# print(img)

##print some image pixels
for i in range(100): 
    for j in range(img.shape[1]): 
       img[i,j] = [255,255,255] # img[i,j] = [0,0,0] #img[i,j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
 
for i in range(img.shape[0]): 
    for j in range(100): 
       img[i,j] = [255,255,255] # img[i,j] = [0,0,0] #img[i,j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

