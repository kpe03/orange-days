import pygame
import json

import math
import utils.config


class Spritesheet:
    #creates a single spritesheet from an image
    def __init__(self, fileName):
        try:
            self.sheet = pygame.image.load(fileName).convert_alpha()
            if not self.sheet.get_alpha():
                self.sheet.set_colorKey((0,0,0))
        except pygame.error:
            print("unable to load spritesheet")

        self.tile_width = math.floor(self.sheet.get_width() / utils.config.TILE_SIZE)
        self.tile_height = math.floor(self.sheet.get_height() / (utils.config.TILE_SIZE))
        
    def getImage(self, tileNum):
        image = pygame.Surface([utils.config.TILE_SIZE, utils.config.TILE_SIZE], pygame.SRCALPHA)

        x = (tileNum % (self.tile_width) * utils.config.TILE_SIZE) 
        y = (math.floor(tileNum / (self.tile_width))) * (utils.config.TILE_SIZE)
        
        #blits the sprite onto new image. image is now a pygame.Rect
        image.blit(self.sheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE))
        #image.blit(image, (0, 0))
        sizedImage = pygame.transform.scale(image, (utils.config.SCALE, utils.config.SCALE))

        return sizedImage

    #compile list of frames for animations
    def getImageList(self, tileNumList):
        list = []
        for tile in tileNumList:
            list.append(self.getImage(tile))

        return list

#for rendering map
class Map():
    def __init__(self, screen):
        #create a list containing Spritesheet objects
        self.spritesList = self.loadSprites(
            ["assets\Tilesets\Fences.png",
             "assets\Tilesets\Grass.png",
             "assets\Tilesets\Hills.png",
             "assets\Tilesets\Tilled_Dirt.png",
             "assets\Tilesets\Water.png",
             "assets\Tilesets\Wooden House.png"])
        self.map = [] 
        self.screen = screen
    
    def loadSprites(self, list):
        spriteList = {}
        name = ["fences", "grass", "hills", "tilledDirt", "water", "house"]
        i = 0
        for sprite in list:
            #add the sprite with its corresponding name, to the list
            spriteList[name[i]] = Spritesheet(sprite)
            i += 1
        return spriteList

    # #read data from json, render to screen
    # def loadMap(self):
    #     with open(self.fileName) as map:
    #         data = json.load(map)
    #         #check if grass component
    #         if data["water"]:
    #             self.map = data["water"]["map"]
    #             self.renderMap("water")
    #         if data["grass"]:
    #             self.map = data["grass"]["map"]
    #             self.renderMap("grass")
                

    def renderMap(self, type):
        ypos = 0
        for line in self.map:
            xpos = 0
            for tile in line:
                tile = self.spritesList[type].getImage(tile)
                rect = pygame.Rect(xpos * utils.config.SCALE, ypos  * utils.config.SCALE, utils.config.SCALE, utils.config.SCALE)
                self.screen.blit(tile, rect)
                xpos = xpos + 1
            ypos = ypos + 1

# ============
#   Tile
# ============
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite, tileNum):
        super().__init__(groups)
        self.image = sprite.getImage(tileNum).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = self.rect.topleft