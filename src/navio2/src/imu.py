#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import navio

def imu_publisher():
    rospy.init_node('navio2_imu')
    pub = rospy.Publisher('lsm_imu', String)
    rate = rospy.Rate(10)
    imu = navio.lsm9ds1.LSM9DS1()
    
    while not rospy.is_shutdown()
        m9a, m9g, m9m = imu.getMotion9();
        accel_data = " Accel: {:+8.3f}".format(m9a[0]) + ", {:+8.3f}".format(m9a[1]) + ", {:+8.3f}".format(m9a[2])
        gyro_data = " Gyr: {:+8.3f}".format(m9g[0]) + ", {:+8.3f}".format(m9g[1]) + ", {:+8.3f}".format(m9g[2])
        data = accel_data + " " + gyro_data
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ = 'main':
    try:
        imu_publisher()
    except rospy.ROSInterruptException:
        pass
