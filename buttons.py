import RPi.GPIO as GPIO
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print('GPIO buttons initialized')

while True:
	if (GPIO.input(18) == False):
		os.system("shutdown 0")
		break
	if (GPIO.input(17) == False):
		os.system("reboot 0")
		break
	if (GPIO.input(27) == False):
		try:
			os.system("killall feh")
		except:
			pass
	time.sleep(1)
