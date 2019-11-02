import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


gameDisplay = pygame.display.set_mode((1002,672))
pygame.display.set_caption('Barley Works')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
clock = pygame.time.Clock()
bg = pygame.image.load("barleyworksbackground.jpg")


while not gameExit:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    gameDisplay.blit(bg, (0, 0))

    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.draw.line(gameDisplay, blue, [189, 425], [388, 425], 5)
    pygame.draw.rect(gameDisplay, blue, [557, 78, 20, 15])



    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()





