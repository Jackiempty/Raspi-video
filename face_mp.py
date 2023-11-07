import cv2
import mediapipe as mp


# img = cv2.imread('image.jpg')
cap = cv2.VideoCapture(0) 

mp_face_detection = mp.solutions.face_detection   # 建立偵測方法
mp_drawing = mp.solutions.drawing_utils           # 建立繪圖方法

with mp_face_detection.FaceDetection(             # 開始偵測人臉
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   # 將 BGR 顏色轉換成 RGB
        results = face_detection.process(frame2)        # 偵測人臉

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)  # 標記人臉

        cv2.imshow('frame', frame)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()