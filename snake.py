import pygame


class Snake:
    """
    This is class with snake body parameters
    """

    def __init__(self, x = 20, y = 20):
        self._width = 15
        self._height = 15
        self._color = (255, 0, 0)
        self.x = x
        self.y = y


    def draw_snake_element(self, window):
        pygame.draw.rect(window, self._color, (self.x, self.y, self._width, self._height))
