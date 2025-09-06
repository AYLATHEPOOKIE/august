import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("I mean, something's forcing you so, yeah")
screen.fill((250,250,250))
score=0

image={
 "candycrush" : pygame.image.load("candy.jpg"),
 "ludo" : pygame.image.load("ludo.png"),
 "subway" : pygame.image.load("subway.png"),
 "temple" : pygame.image.load("temple.png")}

imagerects={
  "candycrush" : pygame.Rect(10,10,100,100),
    "ludo" : pygame.Rect(120,10,100,100),
    "subway" : pygame.Rect(230,10,100,100),
    "temple" : pygame.Rect(340,10,100,100)}



textrects={
  "candycrush" : pygame.Rect(10,400,100,100),
    "temple" : pygame.Rect(120,450,100,100),
    "ludo" : pygame.Rect(230,400,100,100),
    "subway surfers" : pygame.Rect(340,450,100,100)}

scorematch={
    "candycrush":"candycrush",
    "ludo":"ludo",
    "subway":"subway",
    "temple":"temple"}

for i,j in imagerects.items():
    screen.blit(image[i],(j.x,j.y))

font=pygame.font.SysFont("Rockwell",30)
for i,j in textrects.items():
    text=font.render(i,True,(0,0,0))
    screen.blit(text,(j.x,j.y))


while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()

        if i.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
        
        elif i.type==pygame.MOUSEBUTTONUP:
            pos1=pygame.mouse.get_pos()

            startlabel=None
            endlabel=None
            for i,j in imagerects.items():
                if j.collidepoint(pos):
                    startlabel=i

            for i,j in textrects.items():
                if j.collidepoint(pos1):
                    endlabel=i
            
            if startlabel and endlabel:
                pygame.draw.line(screen,(0,30,50),pos,pos1,10)
                pygame.display.update()

                if scorematch[startlabel]==endlabel:
                    score+=1
                    print("You got it right!")
                    if score==4:
                        print("You got them all!!")
                else:
                    print("Try again!")
                    
            
                    
                



    pygame.display.update()    
        

