import cv2
import numpy as np

def empty(v):
    pass


cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)
# cap = cv2.VideoCapture(0)

cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

img = cv2.imread('test.jpg')
img = cv2.resize(img, (0, 0), fx = 0.4, fy = 0.4)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    
    # ret, img = cap.read()
    # if not ret:
    #     break

    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')

    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)

    cv2.imshow('frame', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break             # 按下 q 鍵停止

