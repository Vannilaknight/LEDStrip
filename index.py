import pigpio
import time

RED = 17
GREEN = 22
BLUE = 24

pi = pigpio.pi()

def LightUp(color, num):
    if num == 255:
        return
    else:
        print(num)
        time.sleep(1)
        pi.set_PWM_dutycycle(color, num + 1)

LightUp(RED, 0)
pi.stop()
