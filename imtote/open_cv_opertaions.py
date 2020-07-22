import cv2 as cv
import numpy as np
from matplotlib import *


class Operations:
    def __init__(self):
        print("new op")

    def loadImage(self,imgpath:str):
        return cv.imread(imgpath)
    
    def loadGrayImage(self,imgpath:str):
        return cv.imread(imgpath,cv.IMREAD_GRAYSCALE)
    
    def togray(self,img):
        return cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    def saveImg(self,img,path:str):
        cv.imwrite(path,img)

    def showImg(self,img,title:str):
        cv.imshow(title,img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def showImgs(self,imgs:list):
        x=0
        for i in imgs:


            cv.imshow(str(x),imgs[x])
            x=x+1
        cv.waitKey(0)
        cv.destroyAllWindows()
        


    def addText(self,img,text:str,size:int,startpoint:(int,int),clr:(int,int,int)):
        cv.putText(img,text,startpoint,cv.FONT_HERSHEY_SIMPLEX,size,clr,2,cv.LINE_AA)

    def drowCircle(self,img,center:(int,int),rad:int,clr:(int,int,int),thikness:int):
        cv.circle(img,center,rad,clr,thikness)
    
    def drowLine(self,img,p1:(int,int),p2:(int,int),clr:(int,int,int),thikness:int):
        cv.line(img,p1,p2,clr,thikness)
    
    def drowrect(self,img,p1:(int,int),p2:(int,int),clr:(int,int,int),thikness:int):
        cv.rectangle(img,p1,p2,clr,thikness)
    
    def showvideo(self,videopath:str):
        cap = cv.VideoCapture('1.mp4')
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:    
                cv.imshow(videopath,frame)
                if cv.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
 
        # Closes all the frames
        cv.destroyAllWindows()

    def copy(self,img,p1:(int,int),p2:(int,int)):
        roi=img[p1[0]:p2[0],p1[1]:p2[1]]
        cv.imshow("hi2",img)
        cv.imshow("hi",roi)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def cut(self,img,p1:(int,int),p2:(int,int)):
        roi=img[p1[0]:p2[0],p1[1]:p2[1]]
        img[p1[0]:p2[0],p1[1]:p2[1]]=(255,255,255)
        cv.imshow("hi2",img)
        cv.imshow("hi",roi)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def graytosimi(self,img):
        img2=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                v=img2[x][y]
                img[x][y]=[v-20,v,v+20]
        return img


