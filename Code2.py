# "Segmentate the image by 3 different colors in RGB and HSV scales in the report"

#Import libraries
import cv2
import numpy as np 

#Read image
img1 = cv2.imread('img_1.jpg')

#Change form BGR to HVS
hsv_img = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#Change form HVS to BGR
rgb_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 

#Color ranges
lower_green = (30,100,50)
upper_green = (80,255,255)
lower_blue = (100,100,50)
upper_blue = (110,255,255)
lower_white = (228,236,237)
upper_white = (255,255,255)

#RGB Masks
mask = cv2.inRange(rgb_img, lower_green, upper_green)
mask2 = cv2.inRange(rgb_img, lower_blue, upper_blue)
mask3 = cv2.inRange(rgb_img, lower_white, upper_white)
#HVS Masks
mask4 = cv2.inRange(hsv_img, lower_green, upper_green)
mask5 = cv2.inRange(hsv_img, lower_blue, upper_blue)
mask6 = cv2.inRange(hsv_img, lower_white, upper_white)
#Masks additions
final_mask = mask + mask2 + mask3
final_mask2 = mask4 + mask5 + mask6
#Final images
final_img = cv2.bitwise_and(img1, img1, mask = final_mask)
final_img2 = cv2.bitwise_and(img1, img1, mask = final_mask2)
#Print results
cv2.imshow('Originial Image', img1)
cv2.imshow('HSV', hsv_img)
cv2.imshow('RGB', rgb_img)
cv2.imshow('Bitwise RGB And', final_img)
cv2.imshow('Bitwise HSV And', final_img2)

# To keep open the windows forever
cv2.waitKey(0)
cv2.destroyAllWindows()