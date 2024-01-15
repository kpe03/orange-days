import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, position, group):
        super().__init__(group)
        self.position = position

    def getPosition(self):
        return self.position
    
