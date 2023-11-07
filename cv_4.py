import cv2
import numpy as np
import matplotlib.pyplot as plt


# Open the video file

img = cv2.imread('image_1.png')
img = cv2.resize(img, (0, 0), fx = 0.4, fy = 0.4)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h_min = 16
h_max = 35
s_min = 79
s_max = 255
v_min = 101
v_max = 255
lower = np.array([h_min, s_min, v_min])
upper = np.array([h_max, s_max, v_max])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask = mask)
# lane_image = np.copy(frame)
    

# Display the processed frame
cv2.imshow('Video', img)
cv2.imshow('mask', mask)
cv2.imshow('yellow', result)

cv2.waitKey(0)