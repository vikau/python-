import pygame
from pygame.locals import *
from sys import exit

from random import *

pygame.init()

screen = pygame.display.set_mode((640,480))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    r_color = (randint(0,255),randint(0,255),randint(0,255))

    r_pos = (randint(0,639),randint(0,479))

    r_rad = randint(1,70)

    pygame.draw.circle(screen,r_color,r_pos,r_rad)
    #pygame.draw.line(screen, r_color, (60, 60), (120, 60))

    pygame.display.update()
    
