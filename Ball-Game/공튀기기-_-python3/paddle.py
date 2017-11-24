#!/usr/bin/python
# -*- coding: utf8 -*-
#
# Multimediaprogrammering i Python ST2010
# written by Jonatan Jansson, Anders Hassis & Johan Nenzén
# using Python 3.6.3
#

import pygame
from pygame.locals import *

class Paddle:
    def __init__(self, surface):
        self.surface = surface
        self.x = 10
        self.x_change=0
        self.y = surface.get_height() - 30
        self.w = 200
        self.h = 10
        self.color = 165, 102, 255
  
       
                              
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.w, self.h))
   
    def update2(self, a):
        self.x_change=a
        self.x=self.x+self.x_change

    def levelup(self):
        self.w = self.w - 20
