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
    # lane_image = np.copy(frame)
    

    # Display the processed frame
    cv2.imshow('Video', frame)
    

    # Introduce a delay to play the video at normal speed
    # Set the argument to 1 to introduce a small delay (approximately the frame rate)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()