import cv2
cv2.namedWindow("new",cv2.WINDOW_NORMAL)
#获取视频设备
cap=cv2.VideoCapture(0)
while True:
    #从摄像头读取视频帧
    ret,frame=cap.read()
    #将视频帧在窗口中显示
    cv2.imshow('new',frame)
    #等待键盘设备
    key = cv2.waitKey(1)
    if (key & 0xFF == ord('q')):  # & 0xFF 是用来获取低8位的数据
        break
#释放资源
cap.release()
cv2.destroyAllWindows()