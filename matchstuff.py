import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("I mean, nothing's forcing you so, yeah")
screen.fill((250,250,250))

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

font=pygame.font.SysFont("Rockwell",30)
candycrushtext=font.render("Candy Crush",True,(0,0,0))
ludotext=font.render("Ludo",True,(0,0,0))
subwaytext=font.render("Subway Surfers",True,(0,0,0))
templetext=font.render("Temple Run",True,(0,0,0))


while True:

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()

        if i.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,(50,180,200),pos,10,0)
        
        elif i.type==pygame.MOUSEBUTTONUP:
            pos1=pygame.mouse.get_pos()
            pygame.draw.circle(screen,(50,180,200),pos1,10,0)
            pygame.draw.line(screen,(50,180,200),pos,pos1,5)


    pygame.display.update()    
        

