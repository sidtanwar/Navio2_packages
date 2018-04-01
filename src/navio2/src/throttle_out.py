#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import navio2.pwm

#move these constants to ROS parameters later
Throttle_PWM_OUTPUT = 2
SERVO_MIN = 1.250 #ms
SERVO_MAX = 1.750 #ms
SERVO_NEUTRAL = 1.500 #ms

def input_to_ms(input_val):
    ms = SERVO_NEUTRAL + val

    return ms

def drive_throttle_servo(pwm):
    pwm.set_duty_cycle(pwm)
    
def callback(data):
    input_val = data.data
    if input_val > 0.25:
        input_val = 0.25

    if input_val < -0.25:
        input_val = -0.25

    pwm_val = input_to_ms(input_val)

def listener():
    rospy.init_node('navio2_throttle_out');
    rospy.Subscriber('throttle_out', Float32, callback);

    rospy.spin()

def pwm_setup():
    pwm.set_period(50)
    pwm.enable();
    
if __name__ == 'main':
    try:
        pwm_setup()
        listener()
    except rospy.ROSInterruptException:
