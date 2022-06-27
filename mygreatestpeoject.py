import pygame
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

# pygame basic
pygame.init()
width,height = 1280,720
wid,hei=width/2,height/2
screen =pygame.display.set_mode((width,height))
run = True
color = "grey"

linewidth = 1
radius = 10
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21 = wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21 = hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei
#---x---x---x---x---x---x---x---x
# cv basic code
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
# cap.set(15, 0.1)

detector = HandDetector(detectionCon =0.8,maxHands = 1)
#---x---x---x---x--x--x

# loop
while run:
    #pyagme basic
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        color = "yellow"
    elif keys[pygame.K_r]:
        color = "red" 
    elif keys[pygame.K_o]:
        color = "orange"
    elif keys[pygame.K_p]:
        color = "purple" 
    else:
        color = "black" 
            
    
    # cv basic
    _,img = cap.read()
    img  = cv2.flip(img,1)
    hands,img = detector.findHands(img,flipType = False)
    
    if hands:
        hand = hands[0]
        lmlist = hand["lmList"]
        p1 = lmlist[0][0:2]
        p2 = lmlist[1][0:2]
        p3 = lmlist[2][0:2]
        p4 = lmlist[3][0:2]
        p5 = lmlist[4][0:2]
        p6 = lmlist[5][0:2]
        p7 = lmlist[6][0:2]
        p8 = lmlist[7][0:2]
        p9 = lmlist[8][0:2]
        p10 = lmlist[9][0:2]
        p11 = lmlist[10][0:2]
        p12 = lmlist[11][0:2]
        p13 = lmlist[12][0:2]
        p14 = lmlist[13][0:2]
        p15 = lmlist[14][0:2]
        p16 = lmlist[15][0:2]
        p17 = lmlist[16][0:2]
        p18 = lmlist[17][0:2]
        p19 = lmlist[18][0:2]
        p20 = lmlist[19][0:2]
        p21 = lmlist[20][0:2]
        
        x1,y1 = p1
        x2,y2 = p2
        x3,y3 = p3
        x4,y4 = p4
        x5,y5 = p5
        x6,y6 = p6
        x7,y7 = p7
        x8,y8 = p8
        x9,y9 = p9
        x10,y10 = p10
        x11,y11 = p11
        x12,y12 = p12
        x13,y13 = p13
        x14,y14 = p14
        x15,y15 = p15
        x16,y16 = p16
        x17,y17 = p17
        x18,y18 = p18
        x19,y19 = p19
        x20,y20 = p20
        x21,y21 = p21
        fingers = detector.fingersUp(hand)
        print(fingers)
        
        
    #---x---x---x---x---x--x---x
    
    #circles
    pygame.draw.circle(screen,color,(x1,y1),radius)
    pygame.draw.circle(screen,color,(x2,y2),radius)
    pygame.draw.circle(screen,color,(x3,y3),radius)
    pygame.draw.circle(screen,color,(x4,y4),radius)
    pygame.draw.circle(screen,color,(x5,y5),radius)
    pygame.draw.circle(screen,color,(x6,y6),radius)
    pygame.draw.circle(screen,color,(x7,y7),radius)
    pygame.draw.circle(screen,color,(x8,y8),radius)
    pygame.draw.circle(screen,color,(x9,y9),radius)
    pygame.draw.circle(screen,color,(x10,y10),radius)
    pygame.draw.circle(screen,color,(x11,y11),radius)
    pygame.draw.circle(screen,color,(x12,y12),radius)
    pygame.draw.circle(screen,color,(x13,y13),radius)
    pygame.draw.circle(screen,color,(x14,y14),radius)
    pygame.draw.circle(screen,color,(x15,y15),radius)
    pygame.draw.circle(screen,color,(x16,y16),radius)
    pygame.draw.circle(screen,color,(x17,y17),radius)
    pygame.draw.circle(screen,color,(x18,y18),radius)
    pygame.draw.circle(screen,color,(x19,y19),radius)
    pygame.draw.circle(screen,color,(x20,y20),radius)
    pygame.draw.circle(screen,color,(x21,y21),radius)
    
    #--x---x--x--x---x--x--x--x--x--x---x--x--x--x--x--
    #drawing line 
    if True:
        pygame.draw.line(screen,color,(x1,y1),(x2,y2),linewidth)
        pygame.draw.line(screen,color,(x1,y1),(x6,y6),linewidth)
        pygame.draw.line(screen,color,(x1,y1),(x10,y10),linewidth)
        pygame.draw.line(screen,color,(x1,y1),(x14,y14),linewidth)
        pygame.draw.line(screen,color,(x1,y1),(x18,y18),linewidth)
        pygame.draw.line(screen,color,(x2,y2),(x3,y3),linewidth)
        pygame.draw.line(screen,color,(x3,y3),(x4,y4),linewidth)
        pygame.draw.line(screen,color,(x4,y4),(x5,y5),linewidth)
        pygame.draw.line(screen,color,(x6,y6),(x7,y7),linewidth)
        pygame.draw.line(screen,color,(x7,y7),(x8,y8),linewidth)
        pygame.draw.line(screen,color,(x8,y8),(x9,y9),linewidth)
        pygame.draw.line(screen,color,(x10,y10),(x11,y11),linewidth)
        pygame.draw.line(screen,color,(x11,y11),(x12,y12),linewidth)
        pygame.draw.line(screen,color,(x12,y12),(x13,y13),linewidth)
        pygame.draw.line(screen,color,(x14,y14),(x15,y15),linewidth)
        pygame.draw.line(screen,color,(x15,y15),(x16,y16),linewidth)
        pygame.draw.line(screen,color,(x16,y16),(x17,y17),linewidth)
        pygame.draw.line(screen,color,(x18,y18),(x19,y19),linewidth)
        pygame.draw.line(screen,color,(x19,y19),(x20,y20),linewidth)
        pygame.draw.line(screen,color,(x20,y20),(x21,y21),linewidth)
        pygame.draw.line(screen,color,(x6,y6),(x10,y10),linewidth)
        pygame.draw.line(screen,color,(x10,y10),(x14,y14),linewidth)
        pygame.draw.line(screen,color,(x14,y14),(x18,y18),linewidth)
    
    
    #--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--
    #bullet
    
    #---c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c
    #updating
    pygame.display.update()
    cv2.imshow("game",img)
    cv2.waitKey(linewidth)
pygame.quit()