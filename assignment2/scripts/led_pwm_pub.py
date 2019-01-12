#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt8

def led_control_publisher():
	rospy.init_node('led_control_publisher')
	pub=rospy.Publisher('blink',UInt8,queue_size=10)
	rate=rospy.Rate(10)

	while not rospy.is_shutdown():
		blink=UInt8()
		blink.data=input('input a number from 0 to 255 >')
		print blink.data
		pub.publish(blink)
		rate.sleep()

if __name__=='__main__':
	try:
		led_control_publisher()
	except rospy.ROSInterruptException: pass
