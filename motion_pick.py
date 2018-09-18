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

        KneePitch = ["RKneePitch","LKneePitch"]
        kneePitch_angle = [100*TO_RAD]*2
        self.motionProxy.setAngles(KneePitch,kneePitch_angle,velocity)


        HipPitch = ["LHipPitch","RHipPitch"]
        hipPitch_angle = [-40*TO_RAD]*2
        self.motionProxy.setAngles(HipPitch,hipPitch_angle,velocity)
        
        sleep(4)
        # #self.motionProxy.setStiffnesses("Head", 1.0)
        
        # #转动肘关节
        ElbowRoll = ["LElbowRoll","RElbowRoll"]
        elbowRoll_angle = [-70*TO_RAD,70*TO_RAD]
        self.motionProxy.setAngles(ElbowRoll, elbowRoll_angle, velocity)
        sleep(3)
        # # 岔开腿
        HipYawPitch = ["LHipYawPitch","RHipYawPitch"]
        hipYawpitch_angle = [-50 * TO_RAD]*2
        self.motionProxy.setAngles(HipYawPitch, hipYawpitch_angle, velocity)
        # # 完成下蹲和向前倾
        sleep(4)
        self.motionProxy.closeHand("RHand")
        self.motionProxy.closeHand("LHand")

        
        ShoulderPitch = ["RShoulderPitch","LShoulderPitch"]
        shoulderPitch_angle = [110*TO_RAD,90*TO_RAD]
        self.motionProxy.setAngles(ShoulderPitch,shoulderPitch_angle,velocity)

        # # 肩膀
        ShoulderRoll = ["LShoulderRoll","RShoulderRoll"]
        shoulderRoll_angle = [0.0,0.0]
        self.motionProxy.setAngles(ShoulderRoll,shoulderRoll_angle,velocity)
        # #转动肘关节
        ElbowRoll = ["LElbowRoll","RElbowRoll"]
        elbowRoll_angle = [-2*TO_RAD,2*TO_RAD]
        self.motionProxy.setAngles(ElbowRoll, elbowRoll_angle, velocity)
        self.motionProxy.setAngles("LElbowYaw",0*TO_RAD,velocity)
        # # self.motionProxy.setStiffnesses("RArm",1.0)
        # # self.motionProxy.setStiffnesses("LArm",1.0)
        # # self.motionProxy.setStiffnesses("LShoulderRoll",1.0)
        # # self.motionProxy.setStiffnesses("RShoulderRoll",1.0)
        # # self.motionProxy.setStiffnesses("LElbowRoll",1.0)
        # # self.motionProxy.setStiffnesses("RElbowRoll",1.0)
        # # self.motionProxy.setStiffnesses("LWristYaw",1.0)
        # # self.motionProxy.setStiffnesses("RWristYaw",1.0)
        # #self.motionProxy.setExternalCollisionProtectionEnabled("Arms", False)

        sleep(17)
        # #hipYawpitch_angle = [-60 * TO_RAD]*2
        # #self.motionProxy.setAngles(HipYawPitch, hipYawpitch_angle, velocity)
        anklePitch_angle = [-60*TO_RAD]*2
        self.motionProxy.setAngles(AnklePitch,anklePitch_angle,velocity*0.5)
        kneePitch_angle = [120*TO_RAD]*2
        self.motionProxy.setAngles(KneePitch,kneePitch_angle,velocity)
        sleep(6)
        hipYawpitch_angle = [-60 * TO_RAD,-58*TO_RAD]
        self.motionProxy.setAngles(HipYawPitch, hipYawpitch_angle, velocity)
        self.motionProxy.openHand("LHand")
        self.motionProxy.openHand("RHand")
        #self.motionProxy.setAngles("RShoulderPitch",90*TO_RAD,velocity)
        sleep(3)
        self.motionProxy.setAngles("RKneePitch",90*TO_RAD,velocity)
        self.motionProxy.setAngles("RAnklePitch",-8*TO_RAD,velocity)
        sleep(3)
        self.motionProxy.closeHand("LHand")
        self.motionProxy.setAngles("RAnkleRoll",3*TO_RAD,velocity*0.8)
        #self.motionProxy.setAngles("LShoulderPitch",25*TO_RAD,velocity)
        #sleep(10)



if __name__ == '__main__':
    IP = "192.168.1.104"
    PORT = 9559
    motion_instance = Pick(IP,PORT)
    motion_instance.do_picking()
