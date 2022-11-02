import cv2
cv2.namedWindow("new",cv2.WINDOW_NORMAL)
img=cv2.imread("./image/3-2.jpg")
cv2.imshow("new",img)
while True:
    key=cv2.waitKey(0)
    print(key)
    print(ord("q"))
    if(key & 0xFF==ord('q')):#& 0xFF 是用来获取低8位的数据
        break
    elif(key & 0xFF ==ord('s')):
        cv2.imwrite("./image/3-2copy.jpg",img)
cv2.destroyAllWindows()