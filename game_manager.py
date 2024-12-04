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

