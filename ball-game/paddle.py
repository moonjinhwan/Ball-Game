import pygame
from pygame.locals import *

class Paddle:
    def __init__(self, surface):
        self.surface = surface
        self.x = 10
        self.y = surface.get_height() - 30
        self.w = 200
        self.h = 10
        self.color = 165, 102, 255
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.w, self.h))

    def moveRight(self):
        self.x += 60
        
        if self.x + self.w >= self.surface.get_width()-10:
            self.x = self.surface.get_width() - self.w - 10
        if self.x < 10:
            self.x = 10

    def moveLeft(self):
        self.x -= 60

        if self.x + self.w >= self.surface.get_width()-10:
            self.x = self.surface.get_width() - self.w - 10
        if self.x < 10:
            self.x = 10

    def levelup(self):
        self.w = self.w - 5
        if self.w < 40:
            self.w = 40

    def bounceGreenItem(self):
        self.w = self.w + 10
        if self.w > 350:
            self.w = 350

    def bounceRedItem(self):
        self.w = self.w - 30
        if self.w < 40:
            self.w = 40

    def reset(self):
        self.w = 200
