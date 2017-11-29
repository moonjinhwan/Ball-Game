import pygame
from pygame.locals import *
class Loding:
    def __init__(self, surface):
        self.surface = surface
    def draw(self):
        font=pygame.font.SysFont('Arial Black', 40)

        loding = font.render("Start Game", True, (255, 0, 0))
        pressSpaceImg = font.render("Press space to start", True, (255, 0, 0))
        self.surface.blit(loding, (self.surface.get_width()/2-120, 70))
        self.surface.blit(pressSpaceImg, (self.surface.get_width()-250, self.surface.get_height()-30))
