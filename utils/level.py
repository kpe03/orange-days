import pygame
import utils.config
from utils.maps.testmap import *
from models.player import Player
from utils.spritesheet import *

#for future:
#handling loading map, camera, sprites, etc.
#draw player here so that camera follows player

class Level:
    def __init__(self):
        #sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group() 

        self.map = Map()
        self.setUp() #creates player
        

    def setUp(self):
        self.loadMap()
        self.player = Player(utils.config.SCREEN_CENTER, self.all_sprites, self.collision_sprites)
        
    def loadMap(self):
        for row_index, row in enumerate(WATER):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                #make a tile object, belonging to all_sprites group
                #map contains list of spritesheet, so get the corresponding spritesheet
                #col is the tileNum listed in testmap
                Tile((x,y), self.all_sprites, self.map.spritesList["water"], col, LAYERS['water'])

        for row_index, row in enumerate(GRASS):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                Tile((x,y), self.all_sprites, self.map.spritesList["grass"], col, LAYERS['ground'])

        #rock for testing collision
        Tile((ROCK["x"], ROCK["y"]), [self.all_sprites, self.collision_sprites], self.map.spritesList["hills"], 39)

    def update(self):
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update()
        

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - utils.config.SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - utils.config.SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.screen.blit(sprite.image, offset_rect)
                    
                