import pygame
from pygame.locals import *

class Wall:
    def __init__(self, surface, xxx_todo_changeme, xxx_todo_changeme1 ):
        (x,y) = xxx_todo_changeme
        (w,h) = xxx_todo_changeme1
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = 200, 0, 128

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.w, self.h))
