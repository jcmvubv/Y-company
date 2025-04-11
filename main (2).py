# i will try to only use stuff i learned in university in order to make a rotating 3d cube

import pygame
from pygame.locals import *
from cube import Cube

ROTATING_SPEED = 0.01

pygame.init()
size = width, height = 620, 540

black = 0,0,0
white = 255,255,255

screen = pygame.display.set_mode(size, RESIZABLE)

clock = pygame.time.Clock()

#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 20)

mycube = Cube((width/4, height/4), (200,200,200))



running = True
rotating = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mycube.set_pos(event.pos)

            if event.button == 2: 
                rotating = not rotating

            # if event.button == 3: 
            #     mycube2.set_pos(event.pos)
                
            
    screen.fill(black)


    mycube.render(screen)
    #mycube2.render(screen)


    if rotating:
        mycube.rotate_x(ROTATING_SPEED)
        mycube.rotate_y(ROTATING_SPEED)
        mycube.rotate_z(ROTATING_SPEED)

        # mycube2.rotate_x(-0.01)
        # mycube2.rotate_y(-0.00)
        # mycube2.rotate_z(-0.01)

    pygame.display.update()
    clock.tick(60)