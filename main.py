"""Capture video from camera."""
import cv2 as cv
import numpy as np
import time
path = 'cascades/haarcascade_frontalface_default.xml'
face_detector = cv.CascadeClassifier(path)

def detect():
    rects = face_detector.detectMultiScale(pic_s,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE)
    for rect in rects: 
        cv.rectangle(pic_s,  rect, 255, 2)


cap = cv.VideoCapture(0)
t0 = time.time()
M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
size = (640, 360)
while True:
# Capture frame-by-frame 
    ret, frame = cap.read()
    pic = cv.cvtColor(frame, 0)
    pic_s = cv.warpAffine(pic, M, size)

    detect()
    cv.imshow('window', pic_s)
    t = time.time()
    t0 = t
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv.destroyAllWindows()