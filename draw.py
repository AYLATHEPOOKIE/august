import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Drawinggggg")
colors=["black","red","orange","yellow","green","cyan","blue","purple","pink"]
draw=False
colourrn=0
white=False
screen.fill((255,255,255))

while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
        
        if i.type==pygame.MOUSEBUTTONDOWN:
            if i.button==1:
                draw=True
                mousepos=i.pos
                pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
            if i.button==1:
                draw=False
                pygame.display.update()

        elif i.type==pygame.MOUSEMOTION:
            if draw:
                mouseposrn=i.pos
                
                if white==True:
                 pygame.draw.line(screen,"white",mousepos,mouseposrn,10)
                elif white==False:
                    pygame.draw.line(screen,colors[colourrn],mousepos,mouseposrn,5)
                
                mousepos=mouseposrn
                pygame.display.update()
        
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_SPACE:
                white=False
                #colourrn+=1
                #if colourrn>len(colors)-1:
                 #   colourrn=0
                colourrn=(colourrn+1)%len(colors)
            if i.key==pygame.K_BACKSPACE:
             white=True
                  



        

