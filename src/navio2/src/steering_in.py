#!/usr/bin/env python
'''RCin ROS Node'''
# license removed for brevity
import rospy
from std_msgs.msg import Int32
import navio2.rcinput

def talker():
    '''Steering input Publisher'''
    rospy.init_node('navio2_steering_in')
    pub = rospy.Publisher('steering_in', Int32)
    rate = rospy.Rate(10) # 10hz

    rcin = navio2.rcinput.RCInput()
    while not rospy.is_shutdown():
        steering = int(rcin.read(0))
        rospy.loginfo(steering)
        pub.publish(steering)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
