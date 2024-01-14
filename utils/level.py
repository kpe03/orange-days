import pygame
import utils.config
from utils.maps.testmap import *
from models.player import Player
from utils.spritesheet import Map
from utils.spritesheet import Tile

#for future:
#handling loading map, camera, sprites, etc.
#draw player here so that camera follows player

class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        #sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group() 

        self.map = Map(self.screen)
        self.setUp() #creates player
        

    def setUp(self):
        self.player = Player(utils.config.SCREEN_CENTER, self.screen, self.all_sprites)

        
    def loadMap(self):
        for row_index, row in enumerate(WATER):
            for col_index, col in enumerate(row):
                x = col_index * utils.config.TILE_SIZE
                y = row_index * utils.config.TILE_SIZE
                #make a tile object, belonging to all_sprites group
                #map contains list of spritesheet, so get the corresponding spritesheet
                #col is the tileNum listed in testmap
                Tile((x,y), self.all_sprites, self.map.spritesList["water"], col)

        for row_index, row in enumerate(GRASS):
            for col_index, col in enumerate(row):
                x = col_index * utils.config.TILE_SIZE
                y = row_index * utils.config.TILE_SIZE
                
                Tile((x,y), self.all_sprites, self.map.spritesList["grass"], col)

    def update(self):
        print(self.player.position)
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