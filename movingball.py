import pygame
from pygame.locals import *
import sys
import time
import random

class Sphere(pygame.sprite.Sprite):

    def __init__(self,color,radius,location):

        pygame.sprite.Sprite.__init__(self)
        self.frame = pygame.Surface((radius*2 , radius*2))
        self.frame.fill((255,255,255))
        pygame.draw.circle(self.frame,color,(radius,radius),radius,0)
        self.rect = self.frame.get_rect()
        self.rect.topleft = location
        self.speed = [2,2]

    def moveSpheres(self,windowsize):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > windowsize[0]:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > windowsize[1]:
            self.speed[1] = -self.speed[1]

    def collide(self,group1):

        if pygame.sprite.spritecollide(self,group1,False):
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]



if __name__ == '__main__':
    pygame.init()
    windowsize = (400,400)
    pygame.display.set_caption('colliding sphere')
    screen = pygame.display.set_mode(windowsize,0,32)
    #screen.fill((255,255,255))
    clock = pygame.time.Clock()

    #background = pygame.Surface(windowsize)
    #background.fill((255,255,255))

    spheres = pygame.sprite.Group()

    locations = [(100,100),(250,75),(75,30),(300,300)]

    for x in locations:
        color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        radius = 25
        ball = Sphere(color,radius,x)
        spheres.add(ball)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #screen.blit(background,(0,0))
        screen.fill((255,255,255))
        for ball in spheres:
            ball.moveSpheres(windowsize)
            spheres.remove(ball)
            ball.collide(spheres)
            spheres.add(ball)
            screen.blit(ball.frame,ball.rect)
        pygame.display.update()
        clock.tick(60)
        #time.sleep(0.02)
                                    
