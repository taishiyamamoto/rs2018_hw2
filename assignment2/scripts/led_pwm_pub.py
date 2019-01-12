#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt8

def led_control_publisher():
	rospy.init_node('led_pwm_pub')
	pub=rospy.Publisher('blink',UInt8,queue_size=10)
	rate=rospy.Rate(10)
        while not rospy.is_shutdown():
		blink=UInt8()
		blink.data=rospy.get_param('/led_pwm_pub/led_value')
		rospy.loginfo("%d",blink.data)
		pub.publish(blink)
		rate.sleep()

if __name__=='__main__':
	try:
		led_control_publisher()
	except rospy.ROSInterruptException: pass
