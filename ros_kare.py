#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math
PI=math.pi

rospy.init_node("pose_pub", anonymous=True)

pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size=1000)

for i in range(4):
    pose = Twist()
    pose.linear.x = 2
    if __name__ == "__main__":
        r = rospy.Rate(0.5)
        r.sleep()
        pub.publish(pose)
    
    pose = Twist()
    pose.angular.z = 90*PI/180
    if __name__ == "__main__":
        r = rospy.Rate(0.5)
        r.sleep()
        pub.publish(pose)
