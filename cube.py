import pygame
from pygame.locals import *
from sys import exit

from random import *

pygame.init()
x = 60
y = 60
x1 = 120
y1 = 60

green = (0, 255, 0)

screen = pygame.display.set_mode((640,480))
x_change =0 
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
            if event.key == pygame.K_RIGHT:
                x_change = 10
                    
                
                    
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0    

    x += x_change
    x1 += x_change
    r_color = (randint(0,255),randint(0,255),randint(0,255))

    r_pos = (randint(0,639),randint(0,479))

    r_rad = randint(1,70)

    #pygame.draw.circle(screen,r_color,r_pos,r_rad)
    pygame.draw.line(screen, r_color, (60,60), (120,60),4)
    pygame.draw.line(screen, r_color, (60, 120), (120, 120),4)
    pygame.draw.line(screen, r_color, (60, 60), (60, 120),4)
    pygame.draw.line(screen, r_color, (120, 60), (120, 120),4)

    pygame.draw.line(screen, r_color, (30, 90), (90,90),4)
    pygame.draw.line(screen, r_color, (30, 150), (90,150),4)
    pygame.draw.line(screen, r_color, (30, 90), (30, 150),4)
    pygame.draw.line(screen, r_color, (90,90), (90,150),4)

    pygame.draw.line(screen, r_color, (60, 60), (30, 90),4)
    pygame.draw.line(screen, r_color, (120, 60), (90,90),4)
    pygame.draw.line(screen, r_color, (60, 120), (30, 150),4)
    pygame.draw.line(screen, r_color, (120, 120), (90,150),4)

    pygame.draw.circle(screen, green , (60, 60),5)
    pygame.draw.circle(screen, green , (120, 60),5)
    pygame.draw.circle(screen, green , (60, 120),5)
    pygame.draw.circle(screen, green , (120, 120),5)


    pygame.draw.circle(screen, green , (30, 90),5)
    pygame.draw.circle(screen, green , (90,90),5)
    pygame.draw.circle(screen, green , (30, 150),5)
    pygame.draw.circle(screen, green , (90,150),5)

    
    

    

    pygame.display.update()
    
