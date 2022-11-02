import cv2
fourcc=cv2.VideoWriter_fourcc(*'XVID')
#里面的参数解释；保存文件路径，fourcc，帧率，分辨率（要和摄像头的分辨率一致，不然保存不上数据）
vw=cv2.VideoWriter('./video/3-5out.mp4',fourcc,25,(1280,720))
cv2.namedWindow("new",cv2.WINDOW_NORMAL)
#获取视频设备
cap=cv2.VideoCapture(0)
while True:
    #从摄像头读取视频帧
    ret,frame=cap.read()
    #将视频帧在窗口中显示
    cv2.imshow('new',frame)
    #写数据到多媒体文件
    vw.write(frame)
    #等待键盘设备
    key = cv2.waitKey(1)
    if (key & 0xFF == ord('q')):  # & 0xFF 是用来获取低8位的数据
        break
#释放资源
vw.release()
cap.release()
cv2.destroyAllWindows()