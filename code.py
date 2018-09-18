import cv2
import numpy as np

frame = cv2.imread('input.png')
#cv2.imshow('Original',frame)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
#cv2.imshow('hsv',hsv)
    
lower_blue = np.array([50,50,50])
upper_blue = np.array([130,255,255])

#lower_green = np.array([30,0,0])
#upper_green = np.array([255,255,255])
    
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(frame,frame, mask= mask)
#res[np.where((res == [255,0,0]).all(axis = 2))] = [255,255,255]
#res[np.where((res == [0,255,0]).all(axis = 2))] = [255,255,255]

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(mask,kernel,iterations = 1)
dilation = cv2.dilate(mask,kernel,iterations = 1)

frame[mask == 255] = [225, 225, 225]

# cv2.imshow('res',res)
#cv2.imshow('Mask',mask)
# cv2.imshow('frame',frame)
#cv2.imshow('Dilation',dilation)

cv2.imwrite('kushawa_output.png',frame)

# k = cv2.waitKey(0)