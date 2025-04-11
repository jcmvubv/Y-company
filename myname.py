import pygame , sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400,500))

font = pygame.font.Font(None, 52)
text_surface = font.render(
            "yousef ayman",True,(255,255,255))

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    screen.blit(text_surface, (30,150))

    pygame.display.update()
