import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 660)
cam.set(4, 500)
faceDetector = cv2.CascadeClassifier('face.xml')

while True:
    retV, frame = cam.read()
    warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(warna, 1.3, 5)

    for (x, y, w, h) in faces :
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,225,63), 2)
        rec_face = warna [y : y + h, x : x + w]
    cv2.imshow('WEBCAM', frame)
    close = cv2.waitKey(1) & 0xFF
    if close == 27 or close == ord ('n') :
        break


cam.release()
cv2.destroyAllWindows()