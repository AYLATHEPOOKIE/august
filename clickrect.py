import pygame
from random import randint

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("oooo colours")
screen.fill((250,250,250))

class rectstart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((300,300))
        self.rect=self.image.get_rect()
        self.rect.x=250
        self.rect.y=250

    def update(self,pos):
        if self.rect.collidepoint(pos):
            r,g,b=randint(50,250),randint(35,250),randint(100,250)
            self.image.fill((r,g,b))

rectangle=rectstart()
group=pygame.sprite.Group()
group.add(rectangle)

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        
        if i.type==pygame.MOUSEBUTTONDOWN:
            rectangle.update(i.pos)
    group.draw(screen)
    pygame.display.update()
    