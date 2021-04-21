import pygame
from window import Window
from snake import Snake


class Game:
    """
    This is class with game main loop
    """

    def __init__(self):
        self._step = 15
        self.snake_elements_list = [Snake(375, 30), Snake(375, 15), Snake(375, 0)]
        self.run = True
        self.movement_flag = 4
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

    def move_snake_body(self):
        for i in range(len(self.snake_elements_list) - 1, 0, -1):
            self.snake_elements_list[i].x = self.snake_elements_list[i - 1].x
            self.snake_elements_list[i].y = self.snake_elements_list[i - 1].y

    def do_game(self):
        while self.run:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            # Key pressed
            self.check_if_key_pressed()
            # Draw snake
            for x in self.snake_elements_list:
                x.draw_snake_element(self.game_window.get_window())
            # Refresh game window
            pygame.display.update()
            # Clear game window
            self.game_window.refill_game_window()
            # Move snake body
            self.move_snake_body()
            # Move snake head
            self.snake_elements_list[0].move_snake_head(self.movement_flag, self._step)

