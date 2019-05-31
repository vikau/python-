import pygame
import random
import animate

import os, sys, pygame, random



width = 480
height = 600

display_width=400
display_height=600

fps = 60

navy= (50,205,50)
grey =(205,201,201)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

black = (0,0,0)
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

#initialize game & create window
pygame.init()
pygame.mixer.init()

music = pygame.mixer.music.load ("bgmusic.mp3") #lost.ogg
pygame.mixer.music.play(-1)

gameDisplay = pygame.display.set_mode((display_width,display_height))
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
score =0

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img,(50,45))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.radius = 22 
        self.rect.centerx = width /2
        self.rect.bottom = height - 10
        self.speedx = 0
        self.shoot_delay =250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.speedx = 0
        self.rect.x += self.speedx
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
            
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8

        """if keystate[pygame.K_SPACE]:
            self.shoot()"""
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bull.add(bullet)
            shoot.play()

    def point(self,count):
        font = pygame.font.Font('cs.ttf',40)
        text = font.render("Score: "+str(count),True,yellow)
        screen.blit(text,(150,15))
        

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy
        self.image.set_colorkey(black)
        
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 /2)
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(3,8)
        self.speedx = random.randrange(-2,3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height +10:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)
            
class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        #self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx =x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center



class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("prstart.ttf", 48)
        
    def update(self):
        self.text = ("GAME OVER")
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (250,300)       
        

class Gameoveresc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font("gamecuben.ttf", 18)
        
    def update(self):
        self.text = "PRESS ESC TO RETURN"
        self.image = self.font.render(self.text, 1, (0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (250,400)

        
#Class Module
class SpaceMenu:

#Define the initalize self options
    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [0, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

#Draw the menu
    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i*self.font.get_height()))
            i+=1

#Menu Input            
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

#Position Menu
    def set_pos(self, x, y):
        self.x = x
        self.y = y

#Font Style        
    def set_font(self, font):
        self.font = font

#Highlight Color        
    def set_highlight_color(self, color):
        self.hcolor = color

#Font Color        
    def set_normal_color(self, color):
        self.color = color

#Font position        
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)

        
        
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def menu_title(text1, font1):
    textSurface = font1.render(text1, True, green)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("gamecuben.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def game():
    global player_img
    global enemy
    global score
    global bullet_img
    global all_sprites
    global bull
    global shoot
    global explosion_anim
    
    back = pygame.image.load('skyimg.png').convert()
    back_rect = back.get_rect()

    player_img = pygame.image.load('player_ship.png').convert()
    bullet_img = pygame.image.load('laserBlue01.png').convert()
    enemy = pygame.image.load('meteor.png').convert()
    # load sound
    shoot = pygame.mixer.Sound('sfx_laser1.ogg')
    exp = pygame.mixer.Sound('explosion.wav')
    pygame.mixer.music.load('spaceship.wav')
    pygame.mixer.music.set_volume(0.4)

    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = []

    for i in range(1,9):
        filename = 'ex{}.png'.format(i)
        img = pygame.image.load(filename).convert()
        img.set_colorkey(white)
        img_lg = pygame.transform.scale(img,(65,65))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img,(27,27))
        explosion_anim['sm'].append(img_sm)
    
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bull = pygame.sprite.Group()
    gameoversprite = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(8):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


    #game loop
    pygame.mixer.music.play(-1)
    running = True

    while running:
        #keep loop running at same speed
        clock.tick(fps)

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    player.shoot()
        all_sprites.update()
        gameoversprite.update()
        screen.fill(black)
        screen.blit(back,back_rect)
        gameoversprite.draw(screen)

        hits = pygame.sprite.groupcollide(mobs,bull,True,True)
        for hit in hits:
            score += 1
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
            exp.play()
            
            expl = Explosion(hit.rect.center,'lg')
            all_sprites.add(expl)
        # check to see if a mob hit the player
        hits = pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_circle)
        if hits:
            gameoversprite.add(Gameover())
            gameoversprite.add(Gameoveresc())
            all_sprites.remove(player)
            #running = False
            
        all_sprites.draw(screen)
        player.point(score)    
        pygame.display.flip()

def quitgame():
    pygame.quit()
    quit()        

def helpp():
    pass

def missionMenu():
    pass

def aboutMenu():
    pass

def option1():
    game()
def option2():
    missionMenu()
def option3():
    aboutMenu()   
def option4():
    pygame.quit()
    sys.exit()
    
def game_intro():
    #global largeText
    background_image = pygame.image.load("space.png").convert()

    
    
    """intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font("cs.ttf",60)
        TextSurf , TextRect = menu_title("Space Shooter",largeText)
        TextRect.center = (250,140)
        #gameDisplay.blit(TextSurf,TextRect)

        screen.blit(background_image, [0, 0])
        button("Start",190,200,100,50,grey,bright_green,game)
        button("Help",190,260,100,50,grey,blue,helpp)
        button("Exit",190,320,100,50,grey,bright_red,quitgame)
        gameDisplay.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(15)"""

    menuTitle = SpaceMenu(
        ["Space Shooter"])
        
    menu = SpaceMenu(
        ["Start", option1],
        ["Help", option2],
        ["About", option3],
        ["Exit", option4])
        
        

    #Title
    menuTitle.center_at(100,120)
    menuTitle.set_font(pygame.font.Font("cs.ttf", 60))
    menuTitle.set_highlight_color((255,255,255))
    
    #Menu settings
    menu.center_at(190, 250)
    menu.set_font(pygame.font.Font("gamecuben.ttf", 32))
    menu.set_highlight_color((0, 255, 0))
    menu.set_normal_color((0,0,0))
    keepGoing = True


    while 1:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Update Menu
        menu.update(events)

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return

        #Draw
        screen.blit(background_image, [0, 0])
        
        
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

    

game_intro()        
game()
pygame.quit()    

            
