
import pygame
pygame.init()
width, height = 700,600
screen = pygame.display.set_mode((width,height))
run = True
i=5
q=5
x,y=width/2,height/2
speedx = 1
speedy = 2
radius = 3
hx = 200
while run:
    
    # for quit the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # move the bars
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and i>5:
        i-=5
    if keys[pygame.K_DOWN]and i<height-(hx+5):
        i+=5
    if keys[pygame.K_w]and q>5:
        q-=5
    if keys[pygame.K_s]and q<height-(hx+5):
        q+=5
    
    # move the ball
    x+=speedx 
    y+=speedy  
    if y>=height-radius:
        speedy = -speedy
    if y<=radius:
        speedy = -speedy
    if x>=width-radius:
        speedx = -speedx
    if x<=radius:
        speedx = -speedx
            
    # collision detection
    if x <=40+radius and y<=q+hx and y>=q:
        speedx = -speedx +0.003
        
    if x >=660-radius and y<=i+hx and y>=i:
        speedx = -speedx 
    
        
    
    #filling screen
    screen.fill("black")
    
    # bars 
    pygame.draw.rect(screen,"white",(10,q,30,hx))
    pygame.draw.rect(screen,"white",(width-40,i,30,hx))
    
    # ball
    pygame.draw.circle(screen,"white",(x,y),radius)
    
    # updating the screen
    pygame.display.update()
    # print(i,q)
          
pygame.quit()