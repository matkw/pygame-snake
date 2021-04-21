import pygame


class Window:
    """
    This is class with game window settings
    """

    def __init__(self):
        pygame.display.set_caption("Snake")
        self._width = 810
        self._height = 600
        self._background = (0, 0, 0)
        self._window = pygame.display.set_mode((800, 600))

    def refill_game_window(self):
        self._window.fill(self._background)

    def get_window(self):
        return self._window

    def get_background(self):
        return self._background

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
