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
   
    def update2(self, a):#키 입력을 받은 후 변수들 값을 업데이트
        self.x_change=a
        self.x+=self.x_change
        if self.x + self.w >= self.surface.get_width()-10: #양쪽 경계선 밖으로 못 나감
            self.x = self.surface.get_width() - self.w - 10 
        if self.x < 10: 
            self.x = 10 

    def levelup(self):
        if self.w!=100:
            self.w = self.w - 20
        else:
            self.w=100    