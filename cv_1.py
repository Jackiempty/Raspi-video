import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    canny = cv2.Canny(blur, 150, 250)
    return canny


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 7)
    return line_image


def region_of_interest(image):
    height = image.shape[0]
    polygon = np.array([
        [(0, height), (100000, height), (0, 0)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


# Open the video file
cap = cv2.VideoCapture(r"/Users/jackiecdp/Desktop/video_confirm/footage_1.mp4")

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    lane_image = np.copy(frame)
    canny_image = canny(lane_image)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    line_image = display_lines(lane_image, lines)
    combo_image = cv2.addWeighted(lane_image, 1, line_image, 1, 1)
    combo_image_2 = cv2.addWeighted(lane_image, 1, line_image, 1, 1)

    # Display the processed frame
    cv2.imshow('Video', combo_image_2)

    # Introduce a delay to play the video at normal speed
    # Set the argument to 1 to introduce a small delay (approximately the frame rate)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

