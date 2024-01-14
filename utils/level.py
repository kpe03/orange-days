import pygame
import utils.config
from models.player import Player
from utils.spritesheet import Map

#for future:
#handling loading map, camera, sprites, etc.
#draw player here so that camera follows player

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        #sprite groups
        self.all_sprites = CameraGroup()
        self.map = Map("utils\\maps\\testmap.json", self.screen)
        self.setUp() #creates player
        

    def setUp(self):
        self.player = Player(utils.config.SCREEN_CENTER, self.screen, self.all_sprites)

    def update(self):
        print(self.player.position)
        self.map.loadMap()
        self.all_sprites.groupDraw(self.player)
        self.all_sprites.update()
        

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def groupDraw(self, player):
        self.offset.x = player.rect.centerx - utils.config.SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - utils.config.SCREEN_HEIGHT / 2

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.animation.image, offset_pos)