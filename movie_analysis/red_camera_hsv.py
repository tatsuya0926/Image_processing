import cv2
import numpy as np

cap=cv2.VideoCapture(1)
while True:
    _, frame=cap.read()
    frame=cv2.resize(frame, (500,300))
    #色空間をHSVに変更
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    h=hsv[:,:,0] 
    s=hsv[:,:,1]
    v=hsv[:,:,2]
    #赤色を持つ要素を白にする
    img=np.zeros(h.shape, dtype=np.uint8)
    img[((h<50) | (h>200)) & (s>100)] = 255
    cv2.imshow('RED Camera', img)
    k=cv2.waitKey(1)
    if k==27 or k==13: break
        
cap.release()
cv2.destroyALLWindows()