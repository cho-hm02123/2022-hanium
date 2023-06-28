#!/usr/bin/env python

""" Scenario

 When the robot arrives at the place where the explosive is, It sets the flag on the Y-Control.
 When Y-Control is completed, put the flag onthe robot arm

"""

import rospy, time
from std_msgs.msg import Int8

# Publish List
pub = rospy.Publisher('arm', Int8, queue_size = 10)

msg = Int8()
msg = 1

rospy.init_node('arm_core')
r = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(msg)
    r.sleep()
