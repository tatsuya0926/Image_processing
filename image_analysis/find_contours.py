import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/Users/miyata-pc/Desktop/Python_AI/OpenCV/flower.jpg") #絶対パス
img = cv2.resize(img, (300,169))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7,7), 0)
im2 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY_INV)[1]

plt.subplot(1,2,1)
plt.imshow(im2, cmap="gray")

cnts = cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]

for pt in cnts:
  x,y,w,h = cv2.boundingRect(pt)
  if w < 30 or w > 200:
    continue
  print(x,y,w,h)
  cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.savefig("find_contours.png", dpi=200)
plt.show()