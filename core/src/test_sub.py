#!/usr/bin/env python 

import rospy, time
from std_msgs.msg import Int8

def callback(data):
    rospy.loginfo(data)

def check():
    rospy.init_node('check', anonymous=True)

    rospy.Subscriber("arm",Int8, callback)

    rospy.spin()

if __name__ == '__main__':
    check()
