import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic

img = cv2.imread("cat.jpg")
mos = mosaic(img, (150,250,2500,1750), 10)

cv2.imwrite("cat-mosaic.png", mos)
plt.imshow(cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
plt.show()