
import sys
# pygame 
import pygame as pygame
import pygame as pg
from pygame import *
# окно 
init()
window = pygame.display.set_mode((1200,650))
pygame.display.set_caption("ping pong")
window.fill((250,250,250))
# персонажи
def ball(x,y):
    global window
    rect = pygame.transform.scale(pygame.image.load("ball.png"),(75,75))
    window.blit(rect, (x, y))
def plate(x,y,player="plate"):
    if player == "plate":
        global window
        rect = pygame.transform.scale(pygame.image.load("plate.png"),(25,50))
        window.blit(rect, (x, y))
def window():
    global window
    rect = pygame.transform.scale(pygame.image.load("fon.png"),(1200,650))
    window.blit(rect, (0, 0))

# переменные
w = False
s = False
dder = 5
ader = 5
da = 5
dp = 5
yplate = 650/2
xplate = 0

clock = pygame.time.Clock()
# игра
while True:
    window.fill((250,250,250))
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w = True
            elif event.key == pygame.K_s:
                s = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w = False
            elif event.key == pygame.K_s:
                s = False
    ball(1,1)
    plate(xplate,yplate)

    pygame.display.flip()
    clock.tick(120)
