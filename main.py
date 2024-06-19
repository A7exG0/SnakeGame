import pygame
import time

pygame.init()

MAX_X = 600
MAX_Y = 600
# Здесь делаем окно игры 
display = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption('Snake Game')

snake_color = (0,0,255)  # rgb(0,0,255)
background_color = (255, 255, 255) #rgb(255, 255, 255)
snake_lose_color = (255, 0, 0) # rgb(255, 0, 0)
# Задаем начальные координаты змейки 
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

game_over = False 
lose_flag = False
clock = pygame.time.Clock()

while(not game_over):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x1_change = -20
                y1_change = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x1_change = 20
                y1_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                y1_change = -20
                x1_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y1_change = 20
                x1_change = 0

    new_x1 = x1 + x1_change 
    new_y1 = y1 + y1_change 

    if new_x1 < 0 or MAX_X <= new_x1: 
        clock.tick(0)
        pygame.draw.rect(display, snake_lose_color, [x1, y1, 20, 20])
        pygame.display.update()
        time.sleep(100)

    if new_y1 < 0 or MAX_Y <= new_y1: 
        clock.tick(0)
        pygame.draw.rect(display, snake_lose_color, [x1, y1, 20, 20])
        pygame.display.update()
        time.sleep(100)

    x1 = new_x1 
    y1 = new_y1 

    clock.tick(5)
    display.fill(background_color) # заливаем все белым
    pygame.draw.rect(display, snake_color, [x1, y1, 20, 20]) # x1, y1 - новая позиция змейки; 20, 20 - размеры кубика
    pygame.display.update()

pygame.quit()
quit()