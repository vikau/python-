import pygame ,sys
from random import *
from pygame.locals import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    mainsurface = pygame.display.set_mode((500,500), 0, 32)
    pygame.display.set_caption("Bouncing ball")
    white = (255,255,255)
    red = (255,0,0)

    #block = pygame.Surface((50,50))
    #rect = block.get_rect()
    #block.fill(red)
    r_color = (randint(0,255),randint(0,255),randint(0,255))
    
    r_rad = 20
    x = 100
    y = 100
    r_pos = (x,y)
    #pygame.draw.circle(mainsurface,r_color,r_pos,r_rad)
    
    
    speedx =0
    speedy =0

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainsurface.fill(white)
        pygame.draw.circle(mainsurface,r_color,r_pos,r_rad)
        if x<=0:
            x = +5
        if x>=500:
            x = -5
        pygame.draw.circle(mainsurface,r_color,r_pos,r_rad)
        pygame.display.update()
        clock.tick(60)

main()        
