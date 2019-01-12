#!/usr/bin/env python
import rospy
import roslib
import subprocess
from std_msgs.msg import UInt8
import wiringpi as w
import time

PIN_LED=25
OUTPUT=1

def callback(blink):
	w.softPwmWrite(PIN_LED,blink.data)

def led_blink():
	subprocess.check_call('gpio export 25 out',shell=True)
	rospy.init_node('led_pwm_subscriber')
	w.wiringPiSetupSys()
	w.pinMode(PIN_LED,OUTPUT)
	w.softPwmCreate(PIN_LED,0,255)
	rospy.Subscriber("blink",UInt8,callback)
	rospy.spin()

if __name__=='__main__':
	led_blink()
