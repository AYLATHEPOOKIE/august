import pygame
pygame.init()

screen=pygame.display.set_mode((216,233))
pygame.display.set_caption("light")

offbulb=pygame.image.load("off.jpg")
screen.blit(offbulb,(0,0))
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        
        if i.type==pygame.MOUSEBUTTONDOWN:
                onbulb=pygame.image.load("on.jpg")
                screen.blit(onbulb,(0,0))
                pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
                offbulb=pygame.image.load("off.jpg")
                screen.blit(offbulb,(0,0))
                pygame.display.update()