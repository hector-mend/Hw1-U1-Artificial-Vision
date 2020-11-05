# "Take a picture with your computer camera cellphone or any device to a background with objects around and"
# "Apply the 5 differents types of basic thresholds"

#Libraries
import cv2
import numpy as np 

#Select the image
image1 = cv2.imread('img_1.jpg')
#Image converted to grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
#Implementation of thresholds
ret, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 
ret, th2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) 
ret, th3 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) 
ret, th4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV) 
ret, th5 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC) 

#Original Image.
cv2.imshow('Originial Image', image1)
#Threshold Binary
cv2.imshow('Binary Threshold', th1) 
#Threshold Binary Inverted
cv2.imshow('Binary Threshold Inverted', th2) 
#Threshold to Zero
cv2.imshow('Set to 0', th3) 
#Threshold to Zero Inverted
cv2.imshow('Set to 0 Inverted', th4) 
#Threshold Truncate
cv2.imshow('Truncated Threshold', th5) 

# To keep open the windows forever
cv2.waitKey(0)
cv2.destroyAllWindows()







