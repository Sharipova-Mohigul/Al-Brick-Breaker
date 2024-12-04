import pygame
from conf import *


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 5)

        self.speed = 5