import pygame
from window import Window
from snake import Snake


class Game:
    """
    This is class with game main loop
    """

    def __init__(self):
        self._step = 15
        self.snake = Snake(20, 30)
        self.run = True
        self.movement_flag = 0
        self.game_window = Window()

    def check_if_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.movement_flag != 2:
            self.movement_flag = 1
        if keys[pygame.K_RIGHT] and self.movement_flag != 1:
            self.movement_flag = 2
        if keys[pygame.K_UP] and self.movement_flag != 4:
            self.movement_flag = 3
        if keys[pygame.K_DOWN] and self.movement_flag != 3:
            self.movement_flag = 4

    def do_game(self):
        while self.run:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            # Key pressed
            self.check_if_key_pressed()
            # Move snake
            self.snake.move_snake(self.movement_flag, self._step)
            # Clear game window
            self.game_window.refill_game_window()
            # Draw snake
            self.snake.draw_snake_element(self.game_window.get_window())
            # Refresh game window
            pygame.display.update()
