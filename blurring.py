import cv2 as cv

img = cv.imread('assets/landscape.png')
cv.imshow('landscape', img)

#Average blurring
average = cv.blur(img,(3,3))  #increasing the kerne; size increases the blur
cv.imshow('Average blur',average)

#Gaussian blur
guass = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',guass)

#median blurring
median = cv.medianBlur(img,3)
cv.imshow('Median blur',median)

#bilateral blurring
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral blur',bilateral)

cv.waitKey(0)