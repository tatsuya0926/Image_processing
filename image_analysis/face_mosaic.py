import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

cascade_file ="/Users/miyata-pc/Desktop/Python_AI/OpenCV/haarcascade_frontalface_alt.xml" #正面の顔を検出するファイル
cascade = cv2.CascadeClassifier(cascade_file) #検出器

img = cv2.imread("family.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_list = cascade.detectMultiScale(img_gray, minSize=(150,150))
if len(face_list) == 0:
    quit()

for (x,y,w,h) in face_list:
    img = mosaic(img,(x,y,x+w,y+h), 10)
    
cv2.imwrite("family-mosaic.png", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()