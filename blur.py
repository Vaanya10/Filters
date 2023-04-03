import cv2
import matplotlib.pyplot as plt
im = cv2.imread('C:/Users/dines/Python folder/Filters/pexels-tobi-620337.jpg')
dst = cv2.GaussianBlur(im,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(dst)
plt.show()
