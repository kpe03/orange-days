import pygame
import utils.config
from models.entity import Entity
from utils.spritesheet import Spritesheet

class Player(Entity):
    def __init__(self, position, screen):
        super(Player, self).__init__(position, screen)
        self.sprite = Spritesheet('assets\Characters\Basic Charakter Spritesheet.png')
        self.animations = self.setUp()
        self.direction = pygame.math.Vector2()
        self.status = 'down'

    def setUp(self):
        self.walk = {
            "up": self.sprite.getImageList([49, 52, 55, 58]),
            "down": self.sprite.getImageList([13, 16, 19, 22]),
            "left": self.sprite.getImageList([119, 122, 125, 128]),
            "right": self.sprite.getImageList([85, 88, 91, 94])
        }
        self.idle = {
            "up": self.sprite.getImage(49),
            "down": self.sprite.getImage(13),
            "left": self.sprite.getImage(119),
            "right": self.sprite.getImage(85)
        }

    #handles input/animation updates
    def update(self):
        self.input() #update input
        self.move() #move sprite

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

    def move(self, dt):
        if self.direction.magnitude > 0:
            self.direction = self.direction.normalize()

        #horizontal movement
        self.position.x += self.direction.x * utils.config.WALK_SPEED * dt