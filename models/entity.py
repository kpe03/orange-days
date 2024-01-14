import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, position, screen, group):
        super().__init__(group)
        self.position = position
        self.screen = screen

    def getPosition(self):
        return self.position
    
