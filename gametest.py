
import pygame
print("I guess it runs it if you import")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
bg = pygame.image.load("barleyworksbackground.jpg")

def loadgametest():
    pygame.init()



    pygame.display.set_caption('Barley Works')






def gameLoop():
    gameExit = False
    clock = pygame.time.Clock()
    while not gameExit:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                gameExit = True
        gameDisplay = pygame.display.set_mode((1002, 672))
        gameDisplay.fill(white)
        gameDisplay.blit(bg, (0, 0))

        #pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
        pygame.draw.line(gameDisplay, blue, [189, 425], [388, 425], 5)
        pygame.draw.rect(gameDisplay, blue, [557, 78, 20, 15])



        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

loadgametest()
gameLoop()