#!/usr/bin/env python
'''Throttle input ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Int32
import navio2.rcinput

def talker():
    '''Throttle input Publisher'''
    rospy.init_node('navio2_throttle_in')
    pub = rospy.Publisher('throttle_in', Int32)
    rate = rospy.Rate(10) # 10hz

    rcin = navio2.rcinput.RCInput()
    while not rospy.is_shutdown():
        throttle = int(rcin.read(1))
        rospy.loginfo(throttle)
        pub.publish(throttle)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
