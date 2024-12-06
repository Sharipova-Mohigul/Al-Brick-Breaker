from random import random
import pygame as pygame
from conf import *


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # the ball spawn aleatory in the width of the screen
        self.rect.center = (random() * WIDTH, HEIGHT / 2)