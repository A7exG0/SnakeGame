import pygame
import random

pygame.init()

### КОНСТАНТЫ
MAX_X = 600
MAX_Y = 600
SNAKE_SIZE =  20
FOOD_RADIUS = SNAKE_SIZE // 2
RECORD_HEIGHT = MAX_Y // 15
snake_color = blue = (0,0,255, 255)  # rgb(0,0,255, 255)
background_color = white = (255, 255, 255, 255) #rgb(255, 255, 255, 255)
snake_lose_color = red = (255, 0, 0, 255) # rgb(255, 0, 0, 255)
food_color = (200, 10, 100, 255) # rgb(200, 10, 100, 255)
black = (0, 0, 0)


### ФУНКЦИИ
def create_food(display):
    while(True):
        # Выходим из цикла, если найдем место для еды
        x = random.randrange(FOOD_RADIUS, MAX_X - FOOD_RADIUS + 1, SNAKE_SIZE)
        y = random.randrange(RECORD_HEIGHT + FOOD_RADIUS, MAX_Y - FOOD_RADIUS + 1, SNAKE_SIZE)
        if display.get_at((x, y)) == white:
            break

    pygame.draw.circle(display, food_color, [x, y], FOOD_RADIUS)
    return x - FOOD_RADIUS, y - FOOD_RADIUS

def display_game_over():
    '''
    Создает панельку меню при проигрыше с возможностью переиграть
    '''
    # Создание Surface для текста
    text_surface = pygame.Surface((300, 100))
    text_surface.fill(blue)  # Заполнение поверхности черным цветом

    # Наносим на на новый Surface текст
    font = pygame.font.SysFont(None, 24)
    text = font.render('Game Over! Press R to Restart', True, white)
    text_surface.blit(text, (30, 20))

    # Выводим созданную менюшку на главный экран 
    display.blit(text_surface, (MAX_X // 4, MAX_Y // 4))
    pygame.display.update()

### ОСНОВНОЙ КОД

# Здесь делаем окно игры 
display = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption('Snake Game')

# Создадим верхню панель для фиксирования результата 
record_surface = pygame.Surface((MAX_X, RECORD_HEIGHT))
record_surface.fill(blue)
display.blit(record_surface, (0, 0))

# Создадим нижнюю игровую панель
game_surface = pygame.Surface((MAX_X, MAX_Y - RECORD_HEIGHT))
game_surface.fill(white)
display.blit(game_surface, (0, RECORD_HEIGHT))

# Задаем начальные координаты змейки и нарисуем ее  
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
record = 0
pygame.draw.rect(display, snake_color, [x1, y1, SNAKE_SIZE, SNAKE_SIZE])

# Нарисуем еду
x_food, y_food = create_food(display)

# Задаем необходимые флаги
running = True 
game_over = False 
eat_food = False

clock = pygame.time.Clock()

# Основной цикл игры
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and x1_change == 0:
                x1_change = -SNAKE_SIZE
                y1_change = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and x1_change == 0:
                x1_change = SNAKE_SIZE
                y1_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w and y1_change == 0:
                y1_change = -SNAKE_SIZE
                x1_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s and y1_change == 0:
                y1_change = SNAKE_SIZE
                x1_change = 0

    new_x1 = x1 + x1_change 
    new_y1 = y1 + y1_change 
    # print(MAX_Y - RECORD_HEIGHT, new_x1, new_y1)
    if new_x1 < 0 or MAX_X <= new_x1: 
        pygame.draw.rect(display, snake_lose_color, [x1, y1, SNAKE_SIZE, SNAKE_SIZE])
        game_over = True

    if new_y1 < RECORD_HEIGHT or MAX_Y <= new_y1: 
        pygame.draw.rect(display, snake_lose_color, [x1, y1, SNAKE_SIZE, SNAKE_SIZE])
        game_over = True

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
                        # Очищаем игровую область 
                        display.blit(game_surface, (0, RECORD_HEIGHT))
                        pygame.display.update()
    else:
        pygame.draw.rect(display, white, [x1, y1, SNAKE_SIZE, SNAKE_SIZE]) # заливаем область, откуда ушла змейка
        x1 = new_x1 
        y1 = new_y1 
        clock.tick(5)
        pygame.draw.rect(display, snake_color, [x1, y1, SNAKE_SIZE, SNAKE_SIZE]) # x1, y1 - новая позиция змейки
        if x1 == x_food and y1 == y_food: 
            record += 1 
            print(record)
            x_food, y_food = create_food(display)
        pygame.display.update()

pygame.quit()
quit()