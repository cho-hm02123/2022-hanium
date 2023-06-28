#!/usr/bin/env python

import rospy, time
from std_msgs.msg import Int8

rospy.init_node('test_pub', anonymous=True)

pub = rospy.Publisher('temperature', Int8, queue_size=10)
pub_msg = Int8()
pub_msg=1

pub_in = int(input())

if pub_in == 1:
    pub.publish(pub_msg)

