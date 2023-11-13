import cv2

# img = cv2.imread('image.jpg')
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier('face_detect.xml')
    faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)
    print(len(faceRect))

    for (x, y, w, h) in faceRect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break             # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()