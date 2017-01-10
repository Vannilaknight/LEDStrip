import pigpio

RED = 17
GREEN = 22
BLUE = 24

pi = pigpio.pi()
pi.set_PWM_dutycycle(RED, 255)
pi.set_PWM_dutycycle(GREEN, 128)
pi.set_PWM_dutycycle(BLUE, 128)

pi.stop()
