import pygame
from math import *
pygame.init()

width, height = 800,700

screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)

e_distance = 200
t_distance = 50
e_angle = 0
t_angle = 0
w = width/2
h = height/2
run = True
while run:
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        h-=1
    if keys[pygame.K_DOWN]:
        h+=1
    if keys[pygame.K_LEFT]:
        w-=1
    if keys[pygame.K_RIGHT]:
        w+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    ex = e_distance*cos(e_angle) + w
    ey = e_distance*sin(e_angle) + h
    e_angle += 0.001
    tx = t_distance*cos(t_angle) +ex
    ty = t_distance*sin(t_angle) +ey 
    t_angle += 0.003
    screen.fill("black")
    pygame.draw.circle(screen,"white",(w,h),50)
    pygame.draw.circle(screen,"white",(ex,ey),20)
    pygame.draw.circle(screen,"white",(tx,ty),6)
    pygame.display.update()
















pygame.quit()