import pigpio
import time
import subprocess

subprocess.call(['./start.sh'])

RED = 17
GREEN = 22
BLUE = 24

pi = pigpio.pi()
pi.set_PWM_dutycycle(RED, 255)
time.sleep(5)
pi.set_PWM_dutycycle(GREEN, 128)
time.sleep(5)
pi.set_PWM_dutycycle(BLUE, 128)

def LightUp(color, num):
    print("Color: " + color)
    if num == 255:
        return
    else:
        time.sleep(1)
        pi.set_PWM_dutycycle(color, num + 1);


LightUp(RED, 0)
pi.stop()
