import pygame
import random

class Block(pygame.sprite.Sprite):

    def __init__(self,screen,color,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.screen = screen
        self.rect = self.image.get_rect()
        self.speedx = random.randint(1,10)
        self.speedy = random.randint(1,5)

    def update(self):
        self.rect.left += self.speedx
        self.rect.top += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left <0:
            self.speedx = -self.speedx
        if self.rect.bottom > self.screen.get_height() or self.rect.top <0:
            self.speedy = -self.speedy

            
        
