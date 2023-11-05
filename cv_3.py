import cv2
import numpy as np
import matplotlib.pyplot as plt


# Open the video file

# cap = cv2.VideoCapture(r"/Users/jackiecdp/Desktop/video_confirm/footage_1.mp4")
cap = cv2.VideoCapture(0)


while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min = 16
    h_max = 35
    s_min = 79
    s_max = 255
    v_min = 101
    v_max = 255
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask = mask)
    # lane_image = np.copy(frame)
    

    # Display the processed frame
    cv2.imshow('Video', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('yellow', result)
    

    # Introduce a delay to play the video at normal speed
    # Set the argument to 1 to introduce a small delay (approximately the frame rate)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()