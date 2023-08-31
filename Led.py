import RPi.GPIO as gpio
import time.sleep as sleep


led=40

gpio.setmode(gpio.BOARD)
gpio.setup(led,gpio.OUT)

try:
 while true:
  gpio.output(led,gpio.HIGH)
  sleep(10)
  gpio.output(led,gpio.LOW)
  sleep(10)
except:
 gpio.cleanup()

