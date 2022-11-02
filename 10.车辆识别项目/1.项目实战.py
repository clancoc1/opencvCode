import numpy as np
import cv2
cap=cv2.VideoCapture("./video/10-1.mp4")
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
bgsubmog=cv2.bgsegm.createBackgroundSubtractorMOG()
cars = []
carno=0
def center(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy

while True:

    ret,frame=cap.read()
    if(ret==True):
        #灰度
        cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #去噪（高斯）
        blur=cv2.GaussianBlur(frame,(3,3),5)
        #去背影
        mask=bgsubmog.apply(blur)
        #腐蚀,去掉图中的小方块
        erode=cv2.erode(mask,kernel)
        #膨胀
        dilate=cv2.dilate(erode,kernel,iterations=2)
        #闭操作，去掉物体内部的小块
        close=cv2.morphologyEx(dilate,cv2.MORPH_CLOSE,kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)
        #查找轮廓
        cnts,h=cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame,(10,600),(1200,600),(255,0,0),3)
        for (i,c) in enumerate(cnts):
            (x,y,w,h)=cv2.boundingRect(c)
            #对车辆的宽和高进行判断，验证是否为有效车辆
            isValid=(w>90)and(h>90)
            if (not isValid):
                continue
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cpoint=center(x,y,w,h)
            cars.append(cpoint)
            cv2.circle(frame,(cpoint),5,(0,0,255),-1)
            for (x,y) in cars:
                print(x,y)
                #要有一条线
                if(y>542) and (y<558):
                    carno+=1
                    cars.remove((x,y))
                    print(carno)


        cv2.putText(frame,"cars count:"+str(carno),(500,60),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        cv2.imshow("video",frame)
        # cv2.imshow("erode",erode)
        # cv2.imshow("dilate", dilate)

    key=cv2.waitKey(1)
    if (key==27):
        break

cap.release()
cv2.destroyAllWindows()