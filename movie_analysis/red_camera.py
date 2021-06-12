import cv2
import numpy as np

cap=cv2.VideoCapture(1)
while True:
    _, frame=cap.read()
    frame=cv2.resize(frame, (500,300))
    frame[:,:,0]=0 #青要素0
    frame[:,:,1]=0 #緑要素0
    cv2.imshow('RED Camera', frame)
    k=cv2.waitKey(1)
    if k==27 or k==13: break
        
cap.release()
cv2.destroyALLWindows()