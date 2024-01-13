import pygame
import json

import math
import utils.config


class Spritesheet:
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
        image = pygame.Surface([utils.config.TILE_SIZE, utils.config.CHAR_HEIGHT], pygame.SRCALPHA)

        x = (tileNum % (self.tile_width) * utils.config.TILE_SIZE) 
        y = (math.floor(tileNum / (self.tile_width))) * (utils.config.TILE_SIZE * 2)
        
        #blits the sprite onto new image. image is now a pygame.Rect
        image.blit(self.sheet, (0, 0), (x, y, utils.config.TILE_SIZE, utils.config.TILE_SIZE * 2))
        #image.blit(image, (0, 0))
        sizedImage = pygame.transform.scale(image, (utils.config.SCALE, utils.config.CH_HEIGHT_SCALE))

        return sizedImage

    #compile list of frames for animations
    def getImageList(self, tileNumList):
        list = []
        for tile in tileNumList:
            list.append(self.getImage(tile))

        return list

#for rendering map
class Map(Spritesheet):
    def __init__(self, fileName, screen):
        super().__init__(fileName)
        self.map = []
        self.screen = screen
    
    #todo: update with json file data
    def loadMap(self, jsonFile):
        with open(jsonFile) as map:
            data = json.load(map)
            
    # #put map file into list
    # def loadMap(self, file):
    #     with open('utils/maps' + file + '.txt') as map:
    #         for line in map:
    #             tiles = []
    #             for i in range(0, len(line) - 1, 2):
    #                 tiles.append(line[i])
    #             self.map.append(tiles)

    def renderMap(self, screen):
        ypos = 0
        for line in self.map:
            xpos = 0
            for tileNum in line:
                tile = self.getImage(int(tileNum))
                rect = pygame.Rect(xpos * utils.config.SCALE, ypos  * utils.config.SCALE, utils.config.SCALE, utils.config.SCALE)
                screen.blit(tile, rect)
                xpos = xpos + 1
            ypos = ypos + 1