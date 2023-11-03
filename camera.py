import cv2

# Open the camera
camera = cv2.VideoCapture(0)
count = 0
while True:
    
    # Capture frame-by-frame
    ret, frame = camera.read()
    if not ret:
        break
    print(count)
    count+=1

    # Display the resulting frame
    cv2.imshow('Camera', frame)
    # Write image to specific path
    # cv2.imwrite('/home/candy/Desktop/Vid1/%d.jpg'%(count),frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the camera
camera.release()
cv2.destroyAllWindows()