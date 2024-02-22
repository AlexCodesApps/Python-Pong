import pygame
from sprite import Sprite

def UpdateInput(key):
    for sprite in Sprite.controllableSprites:
        if key.get(pygame.K_UP):
            sprite.changePos(0, -1)
        if key.get(pygame.K_LEFT):
            sprite.changePos(0, 0)
        if key.get(pygame.K_DOWN):
            sprite.changePos(0, 1)
        if key.get(pygame.K_RIGHT):
            sprite.changePos(0, 0)
