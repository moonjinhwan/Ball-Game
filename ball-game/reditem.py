import random

import pygame
from pygame.locals import *

def randsign():
    if(random.randint(0, 1)):
        return 1
    else:
        return -1
        
class Reditem:
    def __init__(self, surface, xxx_todo_changeme, xxx_todo_changeme1 ):
        (x, y) = xxx_todo_changeme
        (vx,vy) = xxx_todo_changeme1
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = 255, 0, 0
        self.radius = 5
        self.active = True
        
    @staticmethod
    def createRandomItemsAsList2(number, screen):
        reditems = []
            
        for i in range (0,number):
            reditems.append(Reditem(screen, (random.randint(50, 550), random.randint(50, 200)), (randsign()*random.uniform(1.0,3.0),random.uniform(1.0,3.0)) ) )

        return reditems
    
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.y > self.surface.get_height() and self.active == True:
            self.active = False
            return True
        else:
            return False

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (int(self.x), int(self.y)), self.radius)
   
