import cv2
import  numpy as np
def callback():
    pass
cv2.namedWindow("new",cv2.WINDOW_NORMAL)
cv2.createTrackbar('R','new',0,255,callback)
cv2.createTrackbar('G','new',0,255,callback)
cv2.createTrackbar('B','new',0,255,callback)
img=np.zeros((480,640,3),np.uint8)
while True:
    cv2.imshow('new',img)
    r=cv2.getTrackbarPos('R',"new")
    g = cv2.getTrackbarPos('G', "new")
    b= cv2.getTrackbarPos('B', "new")
    img[:]=[b,g,r]
    key = cv2.waitKey(1)
    if (key & 0xFF == ord('q')):  # & 0xFF 是用来获取低8位的数据
        break

cv2.destroyAllWindows()