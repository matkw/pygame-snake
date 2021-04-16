import pygame
from window import Window

pygame.init()
game_window = Window()
run = True

color = (255, 0, 0)
x = 10
y = 30
width = 15
height = 15
krok = 15
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
        y += krok

    if movement_flag == 1:
        x -= krok
    if movement_flag == 2:
        x += krok
    if movement_flag == 3:
        y -= krok
    if movement_flag == 4:
        y += krok

    game_window.get_window().fill((0, 0, 0))
    pygame.draw.rect(game_window.get_window(), color, (x, y, width, height))
    pygame.display.update()
