import pygame
import random

width = 800
height = 600


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

class Player(pygame.sprite.Sprite):
    
    # sprite for the player
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50,50))
        self.image = pygame.image.load('car.jpg').convert()
        self.image.set_colorkey(black)
        #self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2,height / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > height -200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > width:
            self.rect.right = 0
        
#initialize game & create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#game loop

running = True

while running:
    #keep loop running at same speed
    #clock.tick(fps)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
        
    screen.fill(black)
        
    all_sprites.draw(screen)
        
    pygame.display.flip()
    clock.tick(30)

pygame.quit()    

            
