import cv2
import numpy as np
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)
# mouse_callback(1,100,100,16,"666")
cv2.namedWindow("new",cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',640,480)
cv2.setMouseCallback("new",mouse_callback,"123")
img=np.zeros((480,640,3),np.uint8)
while True:
    cv2.imshow('new',img)
    key = cv2.waitKey(1)
    if (key & 0xFF == ord('q')):  # & 0xFF 是用来获取低8位的数据
        break
cv2.destroyAllWindows()