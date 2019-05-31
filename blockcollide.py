import pygame
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

class Block(pygame.sprite.Sprite):

    def __init__(self,color,width,height):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

pygame.init()

score = 0
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

block_list = pygame.sprite.Group()

all_sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block(black,20,15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprite_list.add(block)

player = Block(red,20,15)
all_sprite_list.add(player)

done = False

clock = pygame.time.Clock()

while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    block_hit_list = pygame.sprite.spritecollide(player,block_list,True)

    if len(block_hit_list)>0:
        score += len(block_hit_list)
        print score

    all_sprite_list.draw(screen)

    clock.tick(20)

    pygame.display.update()

pygame.quit()    
    
    



    

    
    
