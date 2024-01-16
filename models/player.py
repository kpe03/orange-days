import pygame
from utils.config import *
import utils.config
from models.entity import Entity
from utils.spritesheet import Spritesheet
from utils.animations import Animation

class Player(Entity):
    def __init__(self, position, group, collision_sprites):
        self.type = "player" #for testing
        super(Player, self).__init__(position, group)
        self.sprite = Spritesheet('assets\Characters\Basic Charakter Spritesheet.png')
        self.animationsList = self.setUp()

        #for animations
        self.status = 'down-idle'
        self.animation = self.animationsList[self.status]
        self.image = self.animation.image

        #position
        self.direction = pygame.math.Vector2()
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(position)
        self.z = LAYERS['main']

        #collision
        self.hitbox = self.rect.copy().inflate(-10, -10)
        self.collision_sprites = collision_sprites
    

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
    
    def update(self):
        self.input() 
        self.checkStatus()
        self.move() 
        #update image
        self.animation = self.animationsList[self.status]
        self.image = self.animation.image
        self.animation.update()

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

    #handles position and hitbox 
    def move(self):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #horizontal movement
        self.position.x += self.direction.x * utils.config.WALK_SPEED
        self.rect.centerx = round(self.position.x)
        self.hitbox.centerx = self.rect.centerx
        self.collision('horizontal')
        #vert
        self.position.y += self.direction.y * utils.config.WALK_SPEED 
        self.rect.centery = round(self.position.y)
        self.hitbox.centery = self.rect.centery
        self.collision('vertical')

    def checkStatus(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('-')[0] + '-idle'
       
    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            #checks if sprite contains attribute hitbox
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    print("Collision")
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.y < 0:
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.position.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.position.y = self.hitbox.centery
    