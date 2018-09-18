# -*- coding: utf-8 -*-  
from naoqi import ALProxy  
from almath import TO_RAD
from time import  sleep
class Pick():
    def __init__(self,IP,PORT):
        self.motionProxy = ALProxy("ALMotion", IP, PORT)
        self.life = ALProxy('ALAutonomousLife',IP,PORT)
    def do_picking(self,velocity=0.02):
        self.life.setState('disabled')  # 设置禁用状态，关闭一切反射
        self.motionProxy.wakeUp()
        self.motionProxy.moveTo(0.1,0,0)
        # 脚踝
        AnklePitch = ["LAnklePitch","RAnklePitch"]
        anklePitch_angle = [-40*TO_RAD]*2
        self.motionProxy.setAngles(AnklePitch,anklePitch_angle,velocity)

        # 膝盖弯曲
        KneePitch = ["RKneePitch","LKneePitch"]
        kneePitch_angle = [85*TO_RAD]*2
        self.motionProxy.setAngles(KneePitch,kneePitch_angle,velocity)

        # 大腿根部弯曲
        HipPitch = ["LHipPitch","RHipPitch"]
        hipPitch_angle = [-60*TO_RAD]*2
        self.motionProxy.setAngles(HipPitch,hipPitch_angle,velocity)
        sleep(8)

        # 左臂伸出，保持平衡
        self.motionProxy.setAngles("LShoulderRoll",50*TO_RAD,velocity)

        # # 右肘往回收
        # self.motionProxy.setAngles("RElbowRoll",80*TO_RAD,velocity)

        # 右肩膀抬起
        self.motionProxy.setAngles("RShoulderPitch",119*TO_RAD,velocity)
        sleep(6)
        self.motionProxy.setAngles("LHipYawPitch", -10*TO_RAD, velocity)
        # # 左腿向内倾斜
        # self.motionProxy.setAngles("LHipRoll",-8*TO_RAD,velocity)
        
        # #左脚踝与地面平行
        # self.motionProxy.setAngles("LAnklePitch",8*TO_RAD,velocity)

        # 右大腿伸出
        
        self.motionProxy.setAngles("RHipRoll",-45*TO_RAD,velocity*1.6)
        
        # 右脚踝
        self.motionProxy.setAngles("RAnkleRoll",20*TO_RAD,velocity)
        sleep(8)
        # 右大腿岔开，右大腿根部伸直
        self.motionProxy.setAngles("RHipPitch",-10*TO_RAD,velocity)
        sleep(1)

        self.motionProxy.setAngles("LAnkleRoll",-10*TO_RAD,velocity*1.4)
        sleep(5)
        self.motionProxy.setAngles("RKneePitch",10*TO_RAD,velocity)
        # self.motionProxy.setAngles("RHipYawPitch", -30 * TO_RAD, velocity)
        # self.motionProxy.setAngles("RHipRoll",5*TO_RAD,velocity)
        # self.motionProxy.setAngles("RAnkleRoll",-20*TO_RAD,velocity)

        # # #转动肘关节
        # ElbowRoll = ["LElbowRoll","RElbowRoll"]
        # elbowRoll_angle = [-70*TO_RAD,70*TO_RAD]
        # self.motionProxy.setAngles(ElbowRoll, elbowRoll_angle, velocity)
        # sleep(3)
        # # # 岔开腿
        # HipYawPitch = ["LHipYawPitch","RHipYawPitch"]
        # hipYawpitch_angle = [-50 * TO_RAD]*2
        # self.motionProxy.setAngles(HipYawPitch, hipYawpitch_angle, velocity)
        # # # 完成下蹲和向前倾
        # sleep(4)
        # self.motionProxy.closeHand("RHand")
        # self.motionProxy.closeHand("LHand")

        
        # ShoulderPitch = ["RShoulderPitch","LShoulderPitch"]
        # shoulderPitch_angle = [110*TO_RAD,40*TO_RAD]
        # self.motionProxy.setAngles(ShoulderPitch,shoulderPitch_angle,velocity)

        # # # 肩膀
        # ShoulderRoll = ["LShoulderRoll","RShoulderRoll"]
        # shoulderRoll_angle = [0.0,0.0]
        # self.motionProxy.setAngles(ShoulderRoll,shoulderRoll_angle,velocity)
        # # #转动肘关节
        # ElbowRoll = ["LElbowRoll","RElbowRoll"]
        # elbowRoll_angle = [-2*TO_RAD,2*TO_RAD]
        # self.motionProxy.setAngles(ElbowRoll, elbowRoll_angle, velocity)
        # self.motionProxy.setAngles("LElbowYaw",0*TO_RAD,velocity)
        # # # self.motionProxy.setStiffnesses("RArm",1.0)
        # # # self.motionProxy.setStiffnesses("LArm",1.0)
        # # # self.motionProxy.setStiffnesses("LShoulderRoll",1.0)
        # # # self.motionProxy.setStiffnesses("RShoulderRoll",1.0)
        # # # self.motionProxy.setStiffnesses("LElbowRoll",1.0)
        # # # self.motionProxy.setStiffnesses("RElbowRoll",1.0)
        # # # self.motionProxy.setStiffnesses("LWristYaw",1.0)
        # # # self.motionProxy.setStiffnesses("RWristYaw",1.0)
        # # #self.motionProxy.setExternalCollisionProtectionEnabled("Arms", False)

        # sleep(17)
        # # #hipYawpitch_angle = [-60 * TO_RAD]*2
        # # #self.motionProxy.setAngles(HipYawPitch, hipYawpitch_angle, velocity)
        # anklePitch_angle = [-60*TO_RAD]*2
        # self.motionProxy.setAngles(AnklePitch,anklePitch_angle,velocity*0.5)
        # kneePitch_angle = [120*TO_RAD]*2
        # self.motionProxy.setAngles(KneePitch,kneePitch_angle,velocity)
        # sleep(6)
        # hipYawpitch_angle = [-62 * TO_RAD]*2
        # self.motionProxy.setAngles(HipYawPitch, hipYawpitch_angle, velocity)
        # self.motionProxy.openHand("LHand")
        # self.motionProxy.openHand("RHand")
        # #self.motionProxy.setAngles("RShoulderPitch",90*TO_RAD,velocity)
        # sleep(3)


        # self.motionProxy.closeHand("LHand")
        # self.motionProxy.setAngles("LShoulderPitch",25*TO_RAD,velocity)
        # #sleep(10)



if __name__ == '__main__':
    IP = "192.168.1.102"
    PORT = 9559
    motion_instance = Pick(IP,PORT)
    motion_instance.do_picking()