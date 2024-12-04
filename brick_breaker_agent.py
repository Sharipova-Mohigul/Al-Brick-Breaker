import pickle
import numpy as np
import pygame


class BrickBreakerAgent:
    def __init__(self, game, policy=None, discount_factor=0.1, learning_rate=0.1, exploitation_ratio=0.9):

        if policy is not None:
            self._q_table = policy
        else:
            position = list(game.positions_space.shape)
            position.append(len(game.action_space))
            self._q_table = np.zeros(position)

        self.discount_factor = discount_factor
        self.learning_rate = learning_rate
        self.exploitation_ratio = exploitation_ratio

    def get_next_step(self, state, game):
        pygame.event.get()
        # Aleatory step
        next_step = np.random.choice(list(game.action_space))