import pygame
from utils.config import *
import utils.config
from models.entity import Entity
from utils.spritesheet import Spritesheet
from utils.animations import Animation

class Player(Entity):
    def __init__(self, position, screen, group):
        super(Player, self).__init__(position, screen, group)
        self.sprite = Spritesheet('assets\Characters\Basic Charakter Spritesheet.png')
        self.animationsList = self.setUp()
        self.status = 'down-idle'
        self.animation = self.animationsList[self.status]
        self.image = self.animation.image
        self.direction = pygame.math.Vector2()
        self.rect = self.image.get_rect(topleft = position)
        self.z = LAYERS['main']
        

    def setUp(self):
        dic = {
            "up": Animation(self.sprite.getImageList([55, 58]), 18),
            "down": Animation(self.sprite.getImageList([19, 22]), 18),
            "right": Animation(self.sprite.getImageList([127, 130]), 18),
            "left": Animation(self.sprite.getImageList([91, 94]), 18),

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
        self.image = self.animation.image
        self.move() #move sprite
        self.animation.update()
        # self.draw()

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
       

    # def draw(self):
    #     self.screen.blit(self.animation.image, self.position)
    