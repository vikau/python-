from pygame import *

init()

width = 640
height = 480

screen = display.set_mode((width,height))
display.set_caption('bounceingball')

clock = time.Clock()
x = 10 
y = 10
dx =1
dy =2

end=False

while not end:
    #check input

    for e in event.get():
        if e.type == QUIT:
            end = True

    x += dx
    y += dy

    if y<0 or y>height - 40:
        dy *= -1
    if x<0 or x>width - 40:
        dx *= -1
    screen.fill((100,100,200))
    draw.ellipse(screen,(0,255,0),(x,y,40,40))
    clock.tick(60)
    display.update()

quit()    





    


