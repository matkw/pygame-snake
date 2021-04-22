import pygame
from random import randint


class Food:
    """
    This is class with food parameters
    """
    _color = (255, 0, 0)
    _step = 20

    def __init__(self):
        self.x = self._step * randint(0, 39) + 10
        self.y = self._step * randint(0, 29) + 10

    def draw_apple(self, window):
        pygame.draw.circle(window, self._color, (self.x, self.y), 10, 0)

    # Generate food randomly on game board
