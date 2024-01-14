import pygame
import utils.config
from models.entity import Entity
from utils.spritesheet import Spritesheet

class Player(Entity):
    def __init__(self, position, screen):
        super(Player, self).__init__(position, screen)
        self.sprite = Spritesheet('assets\Characters\Basic Charakter Spritesheet.png')
        self.animations = self.setUp()
        self.status = 'down-idle'
        self.image = self.animations[self.status]
        self.direction = pygame.math.Vector2()
        

    def setUp(self):
        dic = {
            "up": self.sprite.getImageList([49, 52, 55, 58]),
            "down": self.sprite.getImageList([13, 16, 19, 22]),
            "left": self.sprite.getImageList([119, 122, 125, 128]),
            "right": self.sprite.getImageList([85, 88, 91, 94]),
            "up-idle": self.sprite.getImage(49),
            "down-idle": self.sprite.getImage(13),
            "left-idle": self.sprite.getImage(119),
            "right-idle": self.sprite.getImage(85)
        }
        return dic
    
    #handles input/animation updates
    def update(self):
        self.input() #update input
        self.move() #move sprite
        self.draw()
        print(self.position)

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

    def draw(self):
        self.screen.blit(self.image, self.position)
    