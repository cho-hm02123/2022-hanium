#!/usr/bin/env python

import rospy
from playsound import playsound
from std_msgs.msg import Int8

def speaker_play(data):
    playsound( "/home/hyemin/catkin_ws/src/speaker/src/Tiger.wav" )

def waiting_sub():
    rospy.init_node('speaker', anonymous=True)
    rospy.Subscriber("speaker_core", Int8, speaker_play)
    rospy.spin()

if __name__ == '__main__':
    waiting_sub()
