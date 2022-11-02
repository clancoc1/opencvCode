import cv2
import numpy as np
#打开两个文件
img1=cv2.imread('./image/opencv_search.png')
img2=cv2.imread("./image/opencv_orig.png")
#灰度化
g1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
g2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#创建SIFT特征检测器
sift=cv2.xfeatures2d.SIFT_create()
#计算描述子与特征点
kp1,des1=sift.detectAndCompute(g1,None)
kp2,des2=sift.detectAndCompute(g2,None)
#创建匹配器
index_params=dict(algorithm=1,trees=5)
search_params=dict(checks=50)
flann=cv2.FlannBasedMatcher(index_params,search_params)
#对描述子进行匹配计算
good=[]
matchs=flann.knnMatch(des1,des2,k=2)
for i,(m,n) in enumerate(matchs):
    if m.distance<0.7*n.distance:
        good.append(m)
ret=cv2.drawMatchesKnn(img1,kp1,img2,kp2,[good],None)
cv2.imshow("result",ret)
cv2.waitKey(0)