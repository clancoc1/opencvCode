import cv2
import numpy as np
#默认的是浅拷贝
img=cv2.imread("./image/4-1.jpg")
img_copy=img
#copy是深拷贝
img_copy_=img.copy()
img[10:100,10:100]=[0,0,255]
cv2.imshow("img",img)
cv2.imshow("img_copy",img_copy)
cv2.imshow("img_copy_",img_copy_)
cv2.waitKey(0)

