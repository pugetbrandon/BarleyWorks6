import RPi.GPIO as GPIO

pins = (28, 29, 37, 18, 24, 26, 5, 32, 15, 22)
levelpins = (3, 35)

def setup():
    GPIO.setmode(GPIO.BCM)
    global pins
    for i in range(10):
        GPIO.setup(pins(i), GPIO.OUT)
    for i in range(1):
        GPIO.setup(pins(i), GPIO.IN, pull_up_down=GPIO.PUD_UP)



def setGPIO(components):
    for i in range(7):
        if components[i] is True:
            GPIO.output(pins(i), GPIO.HIGH)
        else:
            GPIO.output(pins(i), GPIO.LO)


def getlevel(level):
    global levelpins
    level[0] = GPIO.input(levelpins(0))
    level[1] = GPIO.input(levelpins(1))
    return level