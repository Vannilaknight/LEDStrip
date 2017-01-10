import pigpio
import time

RED = 17
GREEN = 22
BLUE = 24

pi = pigpio.pi()

pi.set_PWM_dutycycle(RED, 0)
pi.set_PWM_dutycycle(GREEN, 0)
pi.set_PWM_dutycycle(BLUE, 0)

def LightUp(color, num):
    if num == 255:
        return
    else:
        print(num)
        time.sleep(1)
        pi.set_PWM_dutycycle(color, num)
        LightUp(color, num + 1)

LightUp(RED, 0)
pi.stop()
