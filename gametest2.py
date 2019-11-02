
import pygame
import XGPIO
import Graphics
import easytemp
import recipe


import time
#new color
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
lineSize = 5

x = 0


bg = pygame.image.load("barleyworksbackground2.jpg")

#need to energize hoppers and set initial valve position

def endheat2strike(setpoint):
    print("muddyWater")
    state = True
    temperature = easytemp.whattemp()
    if temperature >= setpoint:
        state = False
    return state


def setState(changeComp):
    component = []
    for i in range(7):
        print(i)
        component.append(False)
    for i in range(8,10):
        component.append(True)
    
    for i in changeComp:
        component[i] = True

    print(component)
    return component




def loadgametest():
    pygame.init()
    pygame.display.set_caption('Barley Works')

def checkL():
    state = True
    global x
    if x > 100:
        state = False
        x = 0
        return state

    x = x + 1
    print(x)
    return state

def checkT():
    state = True
    global x
    if x > 100:
        state = False
        x = 0
        return state

    x = x + 1
    print(x, "Take 2")
    return state

def gameLoop(phase, components, setpoint):
    gameExit = False
    clock = pygame.time.Clock()
    state = True

    while state:
    #   for event in pygame.event.get():
    #   state = check()   if event.type ==pygame.QUIT:
    #         gameExit = True
        if phase == "heat2strike":
            state = endheat2strike(setpoint)

        gameDisplay = pygame.display.set_mode((1002, 672))
        gameDisplay.fill(white)
        gameDisplay.blit(bg, (0, 0))
        Graphics.changeGraphics(gameDisplay, components)
        pygame.display.update()
        #time.sleep(10)
        clock.tick(30)

    #pygame.quit()
    #quit()


# SETUP
loadgametest()
XGPIO.setup()
XGPIO.setGPIOhi(1)  #add pin numbers for hoppers
recipe = recipe.getrecipe()   #uncomment when ready to run
# display some sort of setup checklist



#HEAT TO STRIKE TEMPERATURE 1
phase = "heat2strike"
equipMent = [2, 6]  #BP and Heater
stkTemp = recipe[1]   #recipe is never called
components = setState(equipMent)
XGPIO.setGPIOhi(components)  #need to fix how GPIO handles this
heaterSignal = 100
#  easytemp.setheatersignal(heaterSignal)  Need to update easytemp
gameLoop(phase, components, stkTemp)

def endheat2strike(setpoint):
    print("muddyWater")
    state = True
    temperature = easytemp.whattemp()
    if temperature >= setpoint:
        state = False
    return state




#Operation 2

# tLines = [line1, line3]
# tempControl = True
# levelControl = False
# controlOptions = [tempControl, levelControl]
# gameLoop(tLines, controlOptions)

tLines = []
# Operation to show all lines
#for i in range(24):
 #   tLines.append(lineMaster[i])


tempControl = False
levelControl = True
controlOptions = [tempControl, levelControl]
equipMent = ["mashPump", "boilerPump"]
setState(equipMent)
print(Graphics.gPump, " gPump value ")
gameLoop(tLines, controlOptions, equipMent)



