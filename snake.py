import pygame


class Snake:
    """
    This is class with snake body parameters
    """

    def __init__(self, x=20, y=20):
        self._width = 15
        self._height = 15
        self._color = (166, 174, 0)
        self.x = x
        self.y = y

    def draw_snake_element(self, window):
        pygame.draw.rect(window, self._color, (self.x, self.y, self._width, self._height))
        pygame.draw.rect(window, (0, 0, 0), (self.x + 4, self.y + 4, self._width//2, self._height//2))

    def move_snake_head(self, movement_flag, step):
        if movement_flag == 1:
            self.x -= step
        if movement_flag == 2:
            self.x += step
        if movement_flag == 3:
            self.y -= step
        if movement_flag == 4:
            self.y += step
