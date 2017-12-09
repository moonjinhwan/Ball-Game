from reditem import *
from paddle import *

import pygame
from pygame.locals import *

class itemCollisionHandler2:
    _reditems = []
    _objects = []
    
    def __init__(self):
        pass
    
    def addReditem(self, reditem):
        self._reditems.append(reditem)
        return reditem
    
    def addObject(self, object):
        self._objects.append(object)
        return object
    
    def reset(self):
        self._reditems = []
        self._objects = []
    
    def update(self):
        i = 1
        
        for reditem in self._reditems:
            for obj in self._objects:
                if self._reditemOnObject(reditem, obj):
                    return True
                
            for reditem2 in self._reditems[i:]:
                self._reditemOnItem(reditem, reditem2)
                
            i += 1
    
    def _reditemOnObject(self, reditem, obj):
        if reditem.x - reditem.radius > obj.x + obj.w: # If the reditem is to the right of the object...
            if reditem.x - reditem.radius + reditem.vx <= obj.x + obj.w: # AND will collide next time...
                if reditem.y + reditem.vy >= obj.y and reditem.y + reditem.vy <= obj.y + obj.h: # And is correct in Y-axis
                    reditem.vx *= -1
        if reditem.x + reditem.radius < obj.x: # If the ball is to the left of the object... 
            if reditem.x + reditem.radius + reditem.vx >= obj.x: # AND will collide next time...
                if reditem.y + reditem.vy >= obj.y and reditem.y + reditem.vy <= obj.y + obj.h: # And is correct in Y-axis
                    reditem.vx *= -1
        if reditem.y - reditem.radius > obj.y + obj.h: # If the ball is under of the object...
            if reditem.y - reditem.radius + reditem.vy <= obj.y + obj.h: # AND will collide next time...
                if reditem.x + reditem.vx >= obj.x and reditem.x + reditem.vx <= obj.x + obj.w: # And is correct in X-axis
                    reditem.vy *= -1                    
        if reditem.y + reditem.radius < obj.y: # If the ball is above the object...
            if reditem.y + reditem.radius + reditem.vy >= obj.y: # AND will collide next time...
                if reditem.x + reditem.vx >= obj.x and reditem.x + reditem.vx <= obj.x + obj.w: # And is correct in X-axis
                    reditem.vy *= -1
                    if isinstance(obj, Paddle): # Is it the paddle it will collide with?
                        return True
    
    def _reditemOnItem(self, reditem1, reditem2):
        dy = reditem1.y - reditem2.y
        dx = reditem1.x - reditem2.x
        
        sumRad = reditem1.radius + reditem2.radius
        sqrRad = sumRad * sumRad
        
        distSqr = (dy * dy) + (dx * dx)
        
        if distSqr <= sqrRad:
            self._handleredItemOnItemCollision(reditem1, reditem2)
            
    def _handleredItemOnItemCollision(self, reditem1, reditem2):
        tempx = reditem1.x
        tempy = reditem1.y
        reditem1.x = reditem2.x
        reditem1.y = reditem2.y
        reditem2.x = tempx
        reditem2.y = tempy

