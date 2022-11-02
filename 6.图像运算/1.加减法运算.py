import cv2
import numpy as np
cat=cv2.imread('./image/6-1.jpg')
print(cat.shape)
img=np.ones((540,720,3),np.uint8)*100
result=cv2.add(cat,img)
result_sub=cv2.subtract(result,img)
cv2.imshow("result",result)
cv2.imshow("result_sub",result_sub)
cv2.waitKey(0)