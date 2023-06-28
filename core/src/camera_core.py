#!/usr/bin/env python

import rospy, time
from std_msgs.msg import Int8

#Publish List
cam_pub = rospy.Publisher('cam_core', Int8, queue_size=10)
speaker_pub = rospy.Publisher('speaker_core', Int8, queue_size = 10)
gps_pub = rospy.Publisher('gps_core', Int8, queue_size = 10) 
msg = Int8()
msg = 1

def callback(data):
    global cam_pub
    global speaker_pub
    global gps_pub
    global msg

    rospy.logwarn("###### Heat Source Detection ######")
    cam_pub.publish(msg)
    rospy.logwarn("##### Please Check The Video #####")

    rospy.loginfo("+++ Enter 1 for Animals and 2 for Humans +++")
    Enter_data = int(input())

    if Enter_data == 1:
        speaker_pub.publish(msg)
        rospy.loginfo(" +++++ Kicking The Animals Out +++++")

    if Enter_data == 2:
        gps_pub.publish(msg)
        rospy.loginfo( " +++++++ Receive Location +++++++")


def check():
    rospy.init_node('camera_core', anonymous=True)

    rospy.Subscriber("temperature", Int8, callback)

    rospy.spin()

if __name__ == '__main__':
    check()
