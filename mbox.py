import pygame,sys
from pygame.locals import *
import movebox
import random

def main():
    pygame.init()

    width = 600
    height = 600
    block_w = 50
    block_h = 50

    mainSurface = pygame.display.set_mode((width,height))

    pygame.display.set_caption('so many cubes')
    clock = pygame.time.Clock()

    blockgroup = pygame.sprite.Group()

    for x in range(10):
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        myblock = movebox.Block(mainSurface,color,block_w,block_h)
        myblock.rect.x = random.randrange(width-block_w)
        myblock.rect.y = random.randrange(height-block_h)
        blockgroup.add(myblock)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mainSurface.fill((255,255,255))
        blockgroup.update()
        blockgroup.draw(mainSurface)
        clock.tick(60)
        pygame.display.update()

main()        

        
        
        
    
