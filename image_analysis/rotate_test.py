import matplotlib.pyplot as plt
import cv2
from scipy import ndimage

cascade_file ="/Users/miyata-pc/Desktop/Python_AI/OpenCV/haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file) #検出器
img = cv2.imread("girl.jpg")

def face_detect(img):
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  face_list = cascade.detectMultiScale(img_gray, minSize=(300,300))

  for (x,y,w,h) in face_list:
    print("顔の座標",x,y,w,h)
    red = (0,0,255)
    cv2.rectangle(img, (x,y), (x+w, y+h), red, thickness=30)

for i in range(0,9):
  ang = i*10
  print("---"+str(ang)+"---")
  img_r =ndimage.rotate(img,ang)
  face_detect(img_r)
  plt.subplot(3,3,i+1)
  plt.axis("off")
  plt.title("angle="+str(ang))
  plt.imshow(cv2.cvtColor(img_r, cv2.COLOR_BGR2RGB))
  
plt.show()