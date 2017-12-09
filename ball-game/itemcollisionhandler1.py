from greenitem import *
from paddle import *

import pygame
from pygame.locals import *

class itemCollisionHandler1:
    _greenitems = []
    _objects = []
    
    def __init__(self):
        pass
    
    def addGreenitem(self, greenitem):
        self._greenitems.append(greenitem)
        return greenitem
    
    def addObject(self, object):
        self._objects.append(object)
        return object
    
    def reset(self):
        self._greenitems = []
        self._objects = []
    
    def update(self):
        i = 1
        
        for greenitem in self._greenitems:
            for obj in self._objects:
                if self._greenitemOnObject(greenitem, obj):
                    return True
                
            for greenitem2 in self._greenitems[i:]:
                self._greenitemOnItem(greenitem, greenitem2)
                
            i += 1
    
    def _greenitemOnObject(self, greenitem, obj):
        if greenitem.x - greenitem.radius > obj.x + obj.w: # If the greenitem is to the right of the object...
            if greenitem.x - greenitem.radius + greenitem.vx <= obj.x + obj.w: # AND will collide next time...
                if greenitem.y + greenitem.vy >= obj.y and greenitem.y + greenitem.vy <= obj.y + obj.h: # And is correct in Y-axis
                    greenitem.vx *= -1
        if greenitem.x + greenitem.radius < obj.x: # If the ball is to the left of the object... 
            if greenitem.x + greenitem.radius + greenitem.vx >= obj.x: # AND will collide next time...
                if greenitem.y + greenitem.vy >= obj.y and greenitem.y + greenitem.vy <= obj.y + obj.h: # And is correct in Y-axis
                    greenitem.vx *= -1
        if greenitem.y - greenitem.radius > obj.y + obj.h: # If the ball is under of the object...
            if greenitem.y - greenitem.radius + greenitem.vy <= obj.y + obj.h: # AND will collide next time...
                if greenitem.x + greenitem.vx >= obj.x and greenitem.x + greenitem.vx <= obj.x + obj.w: # And is correct in X-axis
                    greenitem.vy *= -1                    
        if greenitem.y + greenitem.radius < obj.y: # If the ball is above the object...
            if greenitem.y + greenitem.radius + greenitem.vy >= obj.y: # AND will collide next time...
                if greenitem.x + greenitem.vx >= obj.x and greenitem.x + greenitem.vx <= obj.x + obj.w: # And is correct in X-axis
                    greenitem.vy *= -1
                    if isinstance(obj, Paddle): # Is it the paddle it will collide with?
                        return True
    
    def _greenitemOnItem(self, greenitem1, greenitem2):
        dy = greenitem1.y - greenitem2.y
        dx = greenitem1.x - greenitem2.x
        
        sumRad = greenitem1.radius + greenitem2.radius
        sqrRad = sumRad * sumRad
        
        distSqr = (dy * dy) + (dx * dx)
        
        if distSqr <= sqrRad:
            self._handlegreenItemOnItemCollision(greenitem1, greenitem2)
            
    def _handlegreenItemOnItemCollision(self, greenitem1, greenitem2):
        tempx = greenitem1.x
        tempy = greenitem1.y
        greenitem1.x = greenitem2.x
        greenitem1.y = greenitem2.y
        greenitem2.x = tempx
        greenitem2.y = tempy

