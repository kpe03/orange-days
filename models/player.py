import pygame
import utils.config
from models.entity import Entity
from utils.spritesheet import Spritesheet
from utils.animations import Animation

class Player(Entity):
    def __init__(self, position, screen):
        super(Player, self).__init__(position, screen)
        self.sprite = Spritesheet('assets\Characters\Basic Charakter Spritesheet.png')
        self.animationsList = self.setUp()
        self.status = 'down'
        self.animation = self.animationsList[self.status]
        self.direction = pygame.math.Vector2()
        

    def setUp(self):
        dic = {
            "up": Animation(self.sprite.getImageList([49, 52, 55, 58])),
            "down": Animation(self.sprite.getImageList([13, 16, 19, 22])),
            "right": Animation(self.sprite.getImageList([121, 124, 127, 130])),
            "left": Animation(self.sprite.getImageList([85, 88, 91, 94])),

            "up-idle": Animation(self.sprite.getImageList([49, 52]), 18),
            "down-idle": Animation(self.sprite.getImageList([13, 16]), 18),
            "right-idle": Animation(self.sprite.getImageList([121, 124]), 18),
            "left-idle": Animation(self.sprite.getImageList([85, 88]), 18)
        }
        return dic
    
    #handles input/animation updates
    def update(self):
        self.input() #update input
        self.checkStatus()
        self.animation = self.animationsList[self.status]
        self.move() #move sprite
        self.animation.update()
        self.draw()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def move(self):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #horizontal movement
        self.position[0] += self.direction.x * utils.config.WALK_SPEED
        self.position[1] += self.direction.y * utils.config.WALK_SPEED 

    def checkStatus(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('-')[0] + '-idle'
            print(self.status)
       

    def draw(self):
        self.screen.blit(self.animation.image, self.position)
    