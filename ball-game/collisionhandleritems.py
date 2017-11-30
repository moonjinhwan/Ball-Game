from item import *
from paddle import *

import pygame
from pygame.locals import *

class CollisionHandlerItems:
    _items = []
    _objects = []
    
    def __init__(self):
        pass
    
    def addItem(self, item):
        self._items.append(item)
        return item
    
    def addObject(self, object):
        self._objects.append(object)
        return object
    
    def reset(self):
        self._items = []
        self._objects = []
    
    def update(self):
        i = 1
        
        for item in self._items:
            for obj in self._objects:
                if self._itemOnObject(item, obj):
                    return True
                
            for item2 in self._items[i:]:
                self._itemOnItem(item, item2)
                
            i += 1
    
    def _itemOnObject(self, item, obj):
        if item.x - item.radius > obj.x + obj.w: # If the item is to the right of the object...
            if item.x - item.radius + item.vx <= obj.x + obj.w: # AND will collide next time...
                if item.y + item.vy >= obj.y and item.y + item.vy <= obj.y + obj.h: # And is correct in Y-axis
                    item.vx *= -1
        if item.x + item.radius < obj.x: # If the item is to the left of the object... 
            if item.x + item.radius + item.vx >= obj.x: # AND will collide next time...
                if item.y + item.vy >= obj.y and item.y + item.vy <= obj.y + obj.h: # And is correct in Y-axis
                    item.vx *= -1
        if item.y - item.radius > obj.y + obj.h: # If the item is under of the object...
            if item.y - item.radius + item.vy <= obj.y + obj.h: # AND will collide next time...
                if item.x + item.vx >= obj.x and item.x + item.vx <= obj.x + obj.w: # And is correct in X-axis
                    item.vy *= -1                    
        if item.y + item.radius < obj.y: # If the item is above the object...
            if item.y + item.radius + item.vy >= obj.y: # AND will collide next time...
                if item.x + item.vx >= obj.x and item.x + item.vx <= obj.x + obj.w: # And is correct in X-axis
                    item.vy *= -1
                    if isinstance(obj, Paddle): # Is it the paddle it will collide with?
                        return True
    
    def _itemOnItem(self, item1, item2):
        dy = item1.y - item2.y
        dx = item1.x - item2.x
        
        sumRad = item1.radius + item2.radius
        sqrRad = sumRad * sumRad
        
        distSqr = (dy * dy) + (dx * dx)
        
        if distSqr <= sqrRad:
            self._handleitemOnitemCollision(item1, item2)
            
    def _handleitemOnItemCollision(self, item1, item2):
        tempx = item1.x
        tempy = item1.y
        item1.x = item2.x
        item1.y = item2.y
        item2.x = tempx
        item2.y = tempy
