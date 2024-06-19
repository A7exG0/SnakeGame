import pygame
import time

pygame.init()

MAX_X = 600
MAX_Y = 600
# Здесь делаем окно игры 
display = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption('Snake Game')


snake_color = blue = (0,0,255)  # rgb(0,0,255)
background_color = white = (255, 255, 255) #rgb(255, 255, 255)
snake_lose_color = (255, 0, 0) # rgb(255, 0, 0)
black = (0, 0, 0)

# Задаем начальные координаты змейки 
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

game_over = False 
lose_flag = False
clock = pygame.time.Clock()

def display_game_over():
    # Создание Surface для текста
    text_surface = pygame.Surface((300, 100))
    text_surface.fill(blue)  # Заполнение поверхности черным цветом

    font = pygame.font.SysFont(None, 24)
    text = font.render('Game Over! Press R to Restart', True, white)
    text_surface.blit(text, (30, 20))

    display.blit(text_surface, (MAX_X // 4, MAX_Y // 4))
    pygame.display.update()

running = True 

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
        # pygame.display.update()
        game_over = True

    if new_y1 < 0 or MAX_Y <= new_y1: 
        clock.tick(0)
        pygame.draw.rect(display, snake_lose_color, [x1, y1, 20, 20])
        # pygame.display.update()
        game_over = True

    x1 = new_x1 
    y1 = new_y1 
    clock.tick(5)

    if game_over:
        display_game_over()
        while(game_over and running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Устанавливаем начальные параметры
                        game_over = False 
                        x1 = 300 
                        y1 = 300    
    else:
        display.fill(background_color) # заливаем все белым
        pygame.draw.rect(display, snake_color, [x1, y1, 20, 20]) # x1, y1 - новая позиция змейки; 20, 20 - размеры кубика
        pygame.display.update()

pygame.quit()
quit()