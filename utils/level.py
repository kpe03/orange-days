import pygame
import utils.config
#for future:
#handling loading map, camera, sprites, etc.
#draw player here so that camera follows player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        #sprite groups
        self.all_sprites = CameraGroup()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

        def draw(self, player):
            self.offset.x = player.direction.x - utils.config.SCREEN_WIDTH / 2
            self.offset.y = player.direction.y - utils.config.SCREEN_HEIGHT / 2

          