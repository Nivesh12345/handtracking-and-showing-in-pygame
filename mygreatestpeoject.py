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
wantdotsonright = True
wantdotsonleft = True
wantlinseonright = True
wantlinseonleft = True
linewidth = 1
radius = 10
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21 = wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21 = hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei
X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21 = wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid
Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15,Y16,Y17,Y18,Y19,Y20,Y21 = hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei,hei
#---x---x---x---x---x---x---x---x
# cv basic code
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
# cap.set(15, 0.1)

detector = HandDetector(detectionCon =0.8,maxHands = 2)
#---x---x---x---x--x--x

# loop
while run:
    #pyagme basic
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:

        for i in range(100):
            color = "yellow"
            color = "green"
            color = "purple"
            color = "red"
            color = "orange"
    elif keys[pygame.K_b]:
        color = "balck" 
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
    for hand in hands:
        # hand = hands[0]
        #for left hand
        if hand["type"]=="Left":
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
        
        #for right hand
        if hand["type"]=="Right":
            lmlist = hand["lmList"]
            P1 = lmlist[0][0:2]
            P2 = lmlist[1][0:2]
            P3 = lmlist[2][0:2]
            P4 = lmlist[3][0:2]
            P5 = lmlist[4][0:2]
            P6 = lmlist[5][0:2]
            P7 = lmlist[6][0:2]
            P8 = lmlist[7][0:2]
            P9 = lmlist[8][0:2]
            P10 = lmlist[9][0:2]
            P11 = lmlist[10][0:2]
            P12 = lmlist[11][0:2]
            P13 = lmlist[12][0:2]
            P14 = lmlist[13][0:2]
            P15 = lmlist[14][0:2]
            P16 = lmlist[15][0:2]
            P17 = lmlist[16][0:2]
            P18 = lmlist[17][0:2]
            P19 = lmlist[18][0:2]
            P20 = lmlist[19][0:2]
            P21 = lmlist[20][0:2]
            
            X1,Y1 = P1
            X2,Y2 = P2
            X3,Y3 = P3
            X4,Y4 = P4
            X5,Y5 = P5
            X6,Y6 = P6
            X7,Y7 = P7
            X8,Y8 = P8
            X9,Y9 = P9
            X10,Y10 = P10
            X11,Y11 = P11
            X12,Y12 = P12
            X13,Y13 = P13
            X14,Y14 = P14
            X15,Y15 = P15
            X16,Y16 = P16
            X17,Y17 = P17
            X18,Y18 = P18
            X19,Y19 = P19
            X20,Y20 = P20
            X21,Y21 = P21
        
    #---x---x---x---x---x--x---x
    
    #circles for left hand
    if wantdotsonleft:
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
    

    #circles for right hand
    if wantdotsonright:
        pygame.draw.circle(screen,color,(X1,Y1),radius)
        pygame.draw.circle(screen,color,(X2,Y2),radius)
        pygame.draw.circle(screen,color,(X3,Y3),radius)
        pygame.draw.circle(screen,color,(X4,Y4),radius)
        pygame.draw.circle(screen,color,(X5,Y5),radius)
        pygame.draw.circle(screen,color,(X6,Y6),radius)
        pygame.draw.circle(screen,color,(X7,Y7),radius)
        pygame.draw.circle(screen,color,(X8,Y8),radius)
        pygame.draw.circle(screen,color,(X9,Y9),radius)
        pygame.draw.circle(screen,color,(X10,Y10),radius)
        pygame.draw.circle(screen,color,(X11,Y11),radius)
        pygame.draw.circle(screen,color,(X12,Y12),radius)
        pygame.draw.circle(screen,color,(X13,Y13),radius)
        pygame.draw.circle(screen,color,(X14,Y14),radius)
        pygame.draw.circle(screen,color,(X15,Y15),radius)
        pygame.draw.circle(screen,color,(X16,Y16),radius)
        pygame.draw.circle(screen,color,(X17,Y17),radius)
        pygame.draw.circle(screen,color,(X18,Y18),radius)
        pygame.draw.circle(screen,color,(X19,Y19),radius)
        pygame.draw.circle(screen,color,(X20,Y20),radius)
        pygame.draw.circle(screen,color,(X21,Y21),radius)
    #--x---x--x--x---x--x--x--x--x--x---x--x--x--x--x--
    #drawing line for left hand 
    if wantlinseonleft:
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
    
    #drawing line for right hand 
    if wantlinseonright:
        pygame.draw.line(screen,color,(X1,Y1),(X2,Y2),linewidth)
        pygame.draw.line(screen,color,(X1,Y1),(X6,Y6),linewidth)
        pygame.draw.line(screen,color,(X1,Y1),(X10,Y10),linewidth)
        pygame.draw.line(screen,color,(X1,Y1),(X14,Y14),linewidth)
        pygame.draw.line(screen,color,(X1,Y1),(X18,Y18),linewidth)
        pygame.draw.line(screen,color,(X2,Y2),(X3,Y3),linewidth)
        pygame.draw.line(screen,color,(X3,Y3),(X4,Y4),linewidth)
        pygame.draw.line(screen,color,(X4,Y4),(X5,Y5),linewidth)
        pygame.draw.line(screen,color,(X6,Y6),(X7,Y7),linewidth)
        pygame.draw.line(screen,color,(X7,Y7),(X8,Y8),linewidth)
        pygame.draw.line(screen,color,(X8,Y8),(X9,Y9),linewidth)
        pygame.draw.line(screen,color,(X10,Y10),(X11,Y11),linewidth)
        pygame.draw.line(screen,color,(X11,Y11),(X12,Y12),linewidth)
        pygame.draw.line(screen,color,(X12,Y12),(X13,Y13),linewidth)
        pygame.draw.line(screen,color,(X14,Y14),(X15,Y15),linewidth)
        pygame.draw.line(screen,color,(X15,Y15),(X16,Y16),linewidth)
        pygame.draw.line(screen,color,(X16,Y16),(X17,Y17),linewidth)
        pygame.draw.line(screen,color,(X18,Y18),(X19,Y19),linewidth)
        pygame.draw.line(screen,color,(X19,Y19),(X20,Y20),linewidth)
        pygame.draw.line(screen,color,(X20,Y20),(X21,Y21),linewidth)
        pygame.draw.line(screen,color,(X6,Y6),(X10,Y10),linewidth)
        pygame.draw.line(screen,color,(X10,Y10),(X14,Y14),linewidth)
        pygame.draw.line(screen,color,(X14,Y14),(X18,Y18),linewidth)
    #--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--
    #bullet
    
    #---c--c--c--c--c--c--c--c--c--c--c--c--c--c--c--c
    #updating
    pygame.display.update()
    cv2.imshow("game",img)
    cv2.waitKey(linewidth)
pygame.quit()
