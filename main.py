import pygame
from utils.config import GameState
from game import Game

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(60)
    game.update()
    pygame.display.flip()
