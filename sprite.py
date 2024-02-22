from dataclasses import dataclass
import pygame

@dataclass
class Vector2:
    x: int
    y: int

class Sprite:
    spritesArray = []
    controllableSprites = []
    def __init__(self, s, w, h, x, y):
        try:
            self.image = pygame.image.load(s + ".png")
        except:
            print("Error loading texture", s)
            raise SystemExit()
        self.rect = self.image.get_rect()
        self.setPos(x, y)
        self.setRectSize(w, h)
        self.setRectPos()
        Sprite.spritesArray.append(self)

    def setRectSize(self, w, h):
        self.rect.width = w
        self.rect.height = h
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
    def setRectPos(self):
        self.rect.x = self.myPos.x
        self.rect.y = self.myPos.y
    def setPos(self, x, y):
        self.myPos = Vector2(x, y)
    def changePos(self, x, y):
        self.myPos.x += x
        self.myPos.y += y
        self.setRectPos()
    def SetControllable(self):
        Sprite.controllableSprites.append(self)
