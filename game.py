import pygame
from window import Window
from snake import Snake


class Game:
    """
    This is class with game main loop
    """

    def __init__(self):
        pass

    def do_game(self):
        game_window = Window()
        run = True
        snake = Snake(20, 30)
        step = 15
        movement_flag = 0

        while run:
            pygame.time.delay(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                movement_flag = 1
            if keys[pygame.K_RIGHT]:
                movement_flag = 2
            if keys[pygame.K_UP]:
                movement_flag = 3
            if keys[pygame.K_DOWN]:
                movement_flag = 4

            if movement_flag == 1:
                snake.x -= step
            if movement_flag == 2:
                snake.x += step
            if movement_flag == 3:
                snake.y -= step
            if movement_flag == 4:
                snake.y += step

            game_window.refill_game_window()
            snake.draw_snake_element(game_window.get_window())
            pygame.display.update()
