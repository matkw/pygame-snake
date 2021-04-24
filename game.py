import pygame
from window import Window
from snake import Snake
from food import Food


class Game:
    """
    This is class with game main loop
    """

    def __init__(self):
        self._step = 20
        self.snake_elements_list = [Snake(380, 40), Snake(380, 20), Snake(380, 0)]
        self.run = True
        self.movement_flag = 4
        self.game_window = Window()
        self.food = Food()

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

    def eat_food(self):
        if self.snake_elements_list[0].x == self.food.x - 10 and self.snake_elements_list[0].y == self.food.y - 10:
            self.snake_elements_list.append(Snake(-100, -100))
            self.food = Food()

    def if_collision(self):  # check this
        if int(self.snake_elements_list[0].x) >= int(self.game_window.get_width()) or int(
                self.snake_elements_list[0].x) < 0 \
                or int(self.snake_elements_list[0].y) < 0 or int(self.snake_elements_list[0].y) >= \
                int(self.game_window.get_height()):
            exit(0)

    def if_snake_hit_himself(self):
        for i in range(1, len(self.snake_elements_list), 1):
            if self.snake_elements_list[i].x == self.snake_elements_list[0].x \
                    and self.snake_elements_list[i].y == self.snake_elements_list[0].y:
                exit(0)

    def move_snake_body(self):
        for i in range(len(self.snake_elements_list) - 1, 0, -1):
            self.snake_elements_list[i].x = self.snake_elements_list[i - 1].x
            self.snake_elements_list[i].y = self.snake_elements_list[i - 1].y

    def draw_snake(self):
        for x in self.snake_elements_list:
            x.draw_snake_element(self.game_window.get_window())

    def do_game(self):
        while self.run:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            # Key pressed
            self.check_if_key_pressed()
            # Check if colliion
            self.if_collision()
            # Check if snake hit himself
            self.if_snake_hit_himself()
            # Draw food
            self.food.draw_apple(self.game_window.get_window())
            # Draw snake
            self.draw_snake()
            # Refresh game window
            pygame.display.update()
            # Clear game window
            self.game_window.refill_game_window()
            # Move snake body
            self.move_snake_body()
            # Move snake head
            self.snake_elements_list[0].move_snake_head(self.movement_flag, self._step)
            # Eat food
            self.eat_food()
