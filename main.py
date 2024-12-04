"""
Brick Breaker game in Python using pygame. It will be only one player.
Will use reinforcement learning to learn how to play.

The game is vertical, so the paddle will move left or right.

"""
import pickle

import numpy as np
from brick_breaker_agent import BrickBreakerAgent
import game_manager


def main():
    menu()


def menu():
    # show menu if user want train or use a trained model
    print("Welcome to Brick Breaker!")
    print("1. Train a new model")
    print("2. Use a trained model")
    print("3. Exit")
    option = input("Select an option: ")
    while option not in ['1', '2', '3']:
        option = input("Select an option: ")

    if option == '1':
        print("Training a new model")
        train()
    elif option == '2':
        print("Using a trained model")
        trained_model()
    elif option == '3':
        print("Bye!")
        exit()

def train():
    learner, game = play(rounds=200000, discount_factor=0.2, learning_rate=0.1, exploitation_ratio=0.85,
                         animate=False)
    save_model(game, learner)
