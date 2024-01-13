import pygame
import utils.config
from utils.config import GameState
from game import Game

pygame.init()

screen = pygame.display.set_mode((utils.config.SCREEN_WIDTH, utils.config.SCREEN_HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(60)
    game.update()
    pygame.display.flip()
