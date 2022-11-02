import cv2
import numpy as np
img=np.zeros((480,640,3),np.uint8)
#画线
cv2.line(img,(10,20),(300,400),(0,0,255))
#画椭圆
cv2.ellipse(img,(320,320),(100,50),0,0,360,(0,0,255))
cv2.ellipse(img,(320,320),(100,50),90,45,90,(0,0,255),-1)

#画多边形
pts=np.array([(300,10),(150,100),(450,100)],np.int32)
cv2.polylines(img,[pts],True,(0,0,255))

#画文本
cv2.putText(img,"你好",(10,400),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0))

cv2.imshow('show',img)
cv2.waitKey(0)