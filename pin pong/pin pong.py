
import sys
from random import *
# pygame 
import pygame as pygame
#import pygame as pg
from pygame import *
# окно 
init()
window = pygame.display.set_mode((1200,650))
pygame.display.set_caption("ping pong")
window.fill((250,250,250))
# персонажи
def ball(x,y):
    global window
    # rect = pygame.transform.scale(pygame.image.load("ball.png"),(75,75))
    # window.blit(rect, (x, y))
    circle = pygame.Rect(50, 50, 100, 200)
    pygame.draw.circle(window, (100,250,100), (x,y), 32)
def plate(x,y,player="plate"):
    # if player == "plate":
    #     player = player + ".png"
    #     global window
    #     rect = pygame.transform.scale(pygame.image.load(player),(25,50))
    #     window.blit(rect, (x, y))
    if player == "plate":
        rect = pygame.Surface((25,50))
        rect.fill((50,50,50))
        window.blit(rect, (x,y))
    if player == "vrag":
        rect = pygame.Surface((25,50))
        rect.fill((250,50,50))
        window.blit(rect, (x,y))
def windowq():
    global window
    rect = pygame.transform.scale(pygame.image.load("fon.png"),(1200,650))
    window.blit(rect, (0, 0))
def circler():
    global xball
    global yball
    global yspeed
    global xspeed
    xball = xball + xspeed
    yball = yball + yspeed
    if xball >= 600:
        xspeed = xspeed * -1
        yspeed = yspeed * -1
        if xspeed <= 10:
            xspeed = xspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
        if yspeed <= 10:
            yspeed = yspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
    if xball <= 0:
        xspeed = xspeed * -1
        yspeed = yspeed * -1
        if xspeed <= 10:
            xspeed = xspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
        if yspeed <= 10:
            yspeed = yspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
    if yball >= 0:
        xspeed = xspeed * -1
        yspeed = yspeed * -1
        if xspeed <= 10:
            xspeed = xspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
        if yspeed <= 10:
            yspeed = yspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
    if yball <= 1200:
        xspeed = xspeed * -1
        yspeed = yspeed * -1
        if xspeed <= 10:
            xspeed = xspeed - randint(0,2)
        else:
            xspeed = xspeed + 4
        if yspeed <= 10:
            yspeed = yspeed - randint(0,2)
        else:
            xspeed = xspeed + 4

# переменные
w = False
s = False
dder = 5
ader = 5
da = 5
dp = 5
yplate = 650/2
xplate = 0
yvrag = 650/2
xvrag = 1175
qdder = 5
qader = 5
qda = 5
qdp = 5
sv = False
wv = False
clock = pygame.time.Clock()
xball = 325
yball = 600
xspeed = 2
yspeed = 5
# игра
while True:
    circler()
    window.fill((255,255,255))
    if s and yplate <= 575:
        yplate += ader
        dp = 5
    elif s:
        if da != 0:
            yplate += ader - da
            da -= 0.25
    if w and yplate >= 25:
        yplate -= dder
        da = 5
    elif w:
        if dp != 0:
            yplate -= dder - dp
            dp -= 0.25
        if s and yplate <= 575:
            yplate += ader
            dp = 5
    #
    if sv and yvrag <= 575:
        yvrag += qader
        qdp = 5
    elif sv:
        if da != 0:
            yvrag += qader - qda
            qda -= 0.25
    if wv and yvrag >= 25:
        yvrag -= qdder
        qda = 5
    elif wv:
        if qdp != 0:
            yvrag -= qdder - qdp
            qdp -= 0.25
        if sv and yvrag <= 575:
            yvrag += qader
            qdp = 5


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w = True
            elif event.key == pygame.K_s:
                s = True
            if event.key == pygame.K_UP:
                wv = True
            if event.key == pygame.K_DOWN:
                sv = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w = False
            elif event.key == pygame.K_s:
                s = False
            if event.key == pygame.K_UP:
                wv = False
            if event.key == pygame.K_DOWN:
                sv = False

    ball(yball,xball)
    plate(xplate,yplate,"plate")
    plate(xvrag,yvrag,"vrag")

    pygame.display.flip()
    clock.tick(120)
