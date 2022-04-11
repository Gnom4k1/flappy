import pygame
from pygame.locals import *
import sys
 
pygame.init()
display = pygame.display.set_mode((300, 300))
FPS_CLOCK = pygame.time.Clock()
 
 
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                print("Left Mouse key was clicked")
    pygame.display.update()
    FPS_CLOCK.tick(30)
