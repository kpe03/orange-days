import pygame

class Entity:
    def __init__(self, position, screen):
        self.position = position
        self.screen = screen
        self.traits = None
        
    def updateTraits(self):
        for trait in self.traits.values():
            try: 
                trait.update()
            except AttributeError:
                pass

    def getPosition(self):
        return self.position
    
