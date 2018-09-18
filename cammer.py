#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# This is a tiny example that shows how to show live images from Nao using OpenCV.  
import matplotlib.pyplot as plt
import sys  
import cv2 as cv  
from cv2 import COLOR_RGB2BGRA
from naoqi import ALProxy  
import vision_definitions  
import numpy as np
from numpy import array
from PIL import Image
from almath import TO_RAD
from math import cos,sin
import time
from prediction import prediction

class walking():
    def __init__(self,IP,PORT):
        self.motionProxy  = ALProxy("ALMotion", IP, PORT)
        #self.postureProxy = ALProxy("ALRobotPosture", IP, PORT)
    def doing_walk(self,x = 0.8,y=0.8,theta = 0,frequenty =0.3):
        self.motionProxy.wakeUp()
        #self.postureProxy.goToPosture("StandInit", 0.5)
        #self.set_head_angle()
        self.motionProxy.moveToward(x,y,theta,[["Frequency",frequenty]])
        time.sleep(10)
        self.motionProxy.stopMove()
        #self.motionProxy.rest()
    # def set_head_angle(self):
        # #self.motion=ALProxy('ALMotion', IP, PORT)
        # #self.motion.wakeUp()
        # #self.motion.setStiffnesses("Head", 1.0)
        # angle=20 * TO_RAD
        # direction="HeadPitch"
        # self.motionProxy.setAngles(direction,angle,0.5)
class OpenCVModule():  
    def __init__(self, IP, PORT, CameraID):  
        self._videoProxy = None  
        self._cameraID = CameraID  
        self._resolution = vision_definitions.kVGA  # 640 * 480  
        self._colorSpace = vision_definitions.kBGRColorSpace  
        self._fps = 1  
        self._imgClient = ""  
        self._imgData = None  
        self._registerImageClient(IP, PORT)  
        #self.life = ALProxy('ALAutonomousLife',IP,PORT)
        #self.life.setState('disabled')  # 设置禁用状态，关闭一切反射
        self.motion=ALProxy('ALMotion', IP, PORT)
        time.sleep(1)
        self.set_head_angle()

    def walk(self,x = 0.8,y=0.8,theta = 0,frequenty =0.3):
        self.motion.moveToward(x,y,theta,[["Frequency",frequenty]])
        time.sleep(10) # 让机器人走完这个距离
        self.motion.stopMove()
    def set_head_angle(self):
        
        self.motion.wakeUp()
        self.motion.setStiffnesses("Head", 1.0)
        angle=20 * TO_RAD
        direction="HeadPitch"
        self.motion.setAngles(direction,angle,0.5)
    def _registerImageClient(self, IP, PORT):  
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)  
        self._imgClient = self._videoProxy.subscribeCamera("OpenC", 0, self._resolution, self._colorSpace,self._fps)  
    def _unregisterImageClient(self):  
        if self._imgClient != "":  
            self._videoProxy.unsubscribe(self._imgClient)  

    def showImage(self):
        while True:  
            try:  
                self._imgData = self._videoProxy.getImageRemote(self._imgClient)  
                #time.sleep(2) # 这或许有必要,我不知道从远端拿数据要多长时间
                # 加上判断self._imgData是否为空
                if self._imgData is not None:
                    #print self._imgData
                    
                    #width=self._imgData[0]                                           #列
                    #height=self._imgData[1]                                          #行
                    #self._img=array(self._imgData[6]).astype(int)
                    ima_data=self._imgData[6]                                        #我们要的图像的数据，在第6个元素
                    Nao_ima=array(Image.frombytes('RGB',(self._imgData[0],self._imgData[1]),ima_data))           #opencv的图像存储按BGR格式，要用该库的函数来显示图像，就得把图像转换为BGR格式
                    global COLOR_BGR2RGB
                    Nao_ima= cv.cvtColor(Nao_ima,COLOR_BGR2RGB)
                    if "one" in dir(self):
                        pass
                        
                    else:
                        self.one = prediction()
                    position = self.one.predict(Nao_ima,target)
                        #调用自适应算法
                    #start = time.time()
                    plt.imshow(Nao_ima)
                    plt.show()
                    plt.close('all')
                    #cv.imshow("Camera_OpenCV2", Nao_ima)  
                    #end  = time.time()
                    #print end-start
                    #time.sleep(10)
                    self.walk()
                    #cv.imwrite(r'D:\studyINF\AI\YOLOv3\yolo_img3\background'+'\\'+str(time.time())+'.jpg',Nao_ima)
                    #time.sleep(2) #这或许有必要（停下来之后，立即拿数据），当然要测试过才知道

            except KeyboardInterrupt:  
                print 'Something wrong'
                break  
            #except:
                #pass       #有时候读取不了图像数据 self._imgData是None,为避免多次执行此程序，故 pass掉异常
            time.sleep(2)
            if cv.waitKey(1) == 27:                                             # 按Esc键，就会退出图像
                break
        cv.destroyAllWindows()  
        self._unregisterImageClient()  

if __name__ == '__main__':  
    IP = "192.168.1.104"   
    PORT = 9559  
    CameraID = 0  
    if len(sys.argv) > 1:  
        IP = sys.argv[1]  
    if len(sys.argv) > 2:  
        CameraID = int(sys.argv[2])  
    #mywalk = walking(IP,PORT)
    #mywalk.doing_walk()
    myWidget = OpenCVModule(IP, PORT, CameraID)  
    myWidget.showImage()  
    #print Nao_ima.shape