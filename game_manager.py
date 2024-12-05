import pickle
import numpy as np
import pygame
from brick import Brick
from paddle import Paddle
from ball import Ball
from conf import *
from math import ceil, floor

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
CLOCK = pygame.time.Clock()

def create_sprites():
    all_sprites = pygame.sprite.Group()
    bricks_sprites = pygame.sprite.Group()
    paddle, ball = Paddle(), Ball()

    # Add bricks to sprite groups
    for i in range(BRICK_COLUMNS):
        for j in range(BRICK_ROWS):
            # Create brick cords x and y, spacing between bricks and center the bricks in the screen
            brick = Brick(i * (BRICK_WIDTH + BRICK_SPACING) + BRICK_SPACING + 50,
                          j * (BRICK_HEIGHT + BRICK_SPACING) + BRICK_SPACING + 50)

            all_sprites.add(brick)
            bricks_sprites.add(brick)

    # Add sprites to sprite groups
    all_sprites.add(paddle)
    all_sprites.add(ball)

    return all_sprites, bricks_sprites, ball, paddle


def draw_text(text, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    SCREEN.blit(text_surface, text_rect)


class GameManager:
    def __init__(self):
        self.life = 3
        self.game_over = False

        self.action_space = ['Right', 'Left']
        self.state = [0, 0, 0]
        self._step_penalization = 0
        self.total_reward = 0

        rows = ceil(HEIGHT / 5)
        columns = ceil(WIDTH / 3.75)

        self.positions_space = np.array([[[0 for z in range(columns)]
                                          for y in range(rows)]
                                         for x in range(rows)])

        self.all_sprites, self.bricks_sprites, self.ball, self.paddle = create_sprites()

    def reset(self):
        self.life = 3
        self.game_over = False
        self.state = [0, 0, 0]
        self._step_penalization = 0

        self.all_sprites, self.bricks_sprites, self.ball, self.paddle = create_sprites()

        return self.state

    def step(self, action, animate=False):
        score = self.apply_action(action, animate)
        done = self.life <= 0  # final
        reward = score - self._step_penalization
        self.total_reward += reward
        return self.state, reward, done