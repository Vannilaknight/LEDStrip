import pigpio
import time

RED = 17
GREEN = 22
BLUE = 24

totalTime = 10
currentTime = 0

color1 = [255,0,204]
color2 = [51,204,205]

pi = pigpio.pi()

pi.set_PWM_dutycycle(RED, 0)
pi.set_PWM_dutycycle(GREEN, 0)
pi.set_PWM_dutycycle(BLUE, 0)

def LightDown(color, num):
    if num == 0:
       LightUp(color, num)
    else:
        time.sleep(.1)
        pi.set_PWM_dutycycle(color, num)
        LightDown(color, num - 1)

def LightUp(num):
    if num == totalTime:
        return
    else:
        num += 1
        time.sleep(1)
        interpolate(color1, color2, num/totalTime)
        LightUp(num)

def interpolate(color1, color2, t):
    print("polating")
    r = color1[0] + (color2[0]- color1[0]) * t
    g = color1[1]+ (color2[1]- color1[1]) * t
    b = color1[2] + (color2[2]- color1[2]) * t
    pi.set_PWM_dutycycle(RED, r)
    pi.set_PWM_dutycycle(GREEN, g)
    pi.set_PWM_dutycycle(BLUE, b)

LightUp(0)
pi.stop()
