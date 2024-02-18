import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    def __init__(self, SW):
        super().__init__()
        self.screen = SW.screen
        self.image =  pygame.image.load("images\spirit_breaker.png")
        self.rect = self.image.get_rect()
        self.screen_rect = SW.screen.get_rect()
        self.alien_speed = 0.5

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_alien(self):
        self.y +=  self.alien_speed
        self.rect.y = self.y

    def check_edges(self):
        if self.rect.height >= self.screen_rect.bottom:
            return True    

