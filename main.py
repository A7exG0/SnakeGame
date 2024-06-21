import pygame
import random

pygame.init()

### КОНСТАНТЫ
MAX_X = 600
MAX_Y = 600
SNAKE_SIZE =  20
FOOD_RADIUS = SNAKE_SIZE // 2
RECORD_HEIGHT = MAX_Y // 15
MAX_RECORD = 27
snake_color = blue = (0,0,255, 255)  # rgb(0,0,255, 255)
background_color = white = (255, 255, 255, 255) #rgb(255, 255, 255, 255)
snake_lose_color = red = (255, 0, 0, 255) # rgb(255, 0, 0, 255)
food_color = (200, 10, 100, 255) # rgb(200, 10, 100, 255)
yellow = (255, 255, 0, 255) # rgb(255, 255, 0, 255)  
black = (0, 0, 0)

### КЛАССЫ
class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, coord):
        if isinstance(coord, Coordinate):
            return self.x == coord.x and self.y == coord.y
        return False

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

def display_game_over(record):
    '''
    Создает панельку меню при проигрыше с возможностью переиграть
    '''
    global MAX_RECORD
    # Создание Surface для текста
    text_surface = pygame.Surface((300, 100))
    text_surface.fill(blue)  # Заполнение поверхности синим цветом

    # Наносим на на новый Surface текст
    font = pygame.font.SysFont(None, 24)
    if record <= MAX_RECORD: 
        first_text = font.render(f'Game Over! Your result is {record}', True, white)
        second_text = font.render('Press R to Restart', True, white)
    else:
        MAX_RECORD = record
        first_text = font.render(f'Game Over! Your result is {record}', True, yellow)
        second_text = font.render(f'You have broken the record!', True, yellow)
        third_text = font.render('Press R to Restart', True, yellow)
        text_surface.blit(third_text, (30, 20 + 2 * font.get_linesize()))

    text_surface.blit(first_text, (30, 20))
    text_surface.blit(second_text, (30, 20 + font.get_linesize()))

    # Выводим созданную менюшку на главный экран 
    display.blit(text_surface, (MAX_X // 4, MAX_Y // 4))
    pygame.display.update()

def update_record(record_surface, new_record):
    record_surface.fill(blue)

    font = pygame.font.SysFont("Arial", RECORD_HEIGHT // 2)
    str_record = font.render(str(new_record), True, white)
    str_max_record = font.render(str(MAX_RECORD), True, yellow)

    record_surface.blit(str_record, (RECORD_HEIGHT // 4, RECORD_HEIGHT // 4 ))
    record_surface.blit(str_max_record, (MAX_X // 2, RECORD_HEIGHT // 4))

    return record_surface

def set_default_parameters():
    global x1, y1, x_change, y_change, record, record_surface, display, x_food, y_food, running, game_over, snake
    x1 = y1 = 300
    x_change = 20
    y_change = 0
    record = 1
    record_surface = update_record(record_surface, record)
    display.blit(record_surface, (0, 0))
    pygame.draw.rect(display, snake_color, [x1, y1, SNAKE_SIZE, SNAKE_SIZE])
    x_food, y_food = create_food(display)
    running = True 
    game_over = False 
    snake = [Coordinate(x1, y1)]

### ОСНОВНОЙ КОД

# Здесь делаем окно игры 
display = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption('Snake Game')

# Создадим верхню панель для фиксирования результата 
record_surface = pygame.Surface((MAX_X, RECORD_HEIGHT))
record_surface.fill(blue)

# Создадим нижнюю игровую панель
game_surface = pygame.Surface((MAX_X, MAX_Y - RECORD_HEIGHT))
game_surface.fill(white)
display.blit(game_surface, (0, RECORD_HEIGHT))

# Рисуем бошку для змеи
snake_head = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
snake_head.fill(blue)
pygame.draw.rect(snake_head, red, [4, 4, 4, 8])
pygame.draw.rect(snake_head, red, [12, 4, 4, 8])

# Задаем начальные координаты змейки и нарисуем ее  
set_default_parameters()

clock = pygame.time.Clock()

# Основной цикл игры
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and x_change == 0:
                x_change = -SNAKE_SIZE
                y_change = 0
                break 
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and x_change == 0:
                x_change = SNAKE_SIZE
                y_change = 0
                break
            elif (event.key == pygame.K_UP or event.key == pygame.K_w) and y_change == 0:
                y_change = -SNAKE_SIZE
                x_change = 0
                break
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and y_change == 0:
                y_change = SNAKE_SIZE
                x_change = 0
                break

    new_x = snake[0].x + x_change 
    new_y = snake[0].y + y_change 

    if new_x < 0 or MAX_X <= new_x: 
        pygame.draw.rect(display, snake_lose_color, [snake[0].x, snake[0].y, SNAKE_SIZE, SNAKE_SIZE])
        game_over = True

    if new_y < RECORD_HEIGHT or MAX_Y <= new_y: 
        pygame.draw.rect(display, snake_lose_color, [snake[0].x, snake[0].y, SNAKE_SIZE, SNAKE_SIZE])
        game_over = True

    if game_over:
        display_game_over(record)
        while(game_over and running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Очищаем игровую область 
                        display.blit(game_surface, (0, RECORD_HEIGHT))
                        # Устанавливаем начальные параметры
                        set_default_parameters()
                        pygame.display.update()
    else:
        clock.tick(5)

        head = Coordinate(new_x, new_y)   
        crash_flag = False    
        snake.insert(0, head) # двигаем голову змейки
        for snake_part in snake[1:]: # рисуем всю змею
            if head == snake_part: 
                crash_flag = True 
                break
            pygame.draw.rect(display, snake_color, [snake_part.x, snake_part.y, SNAKE_SIZE, SNAKE_SIZE])

        # если змейка скушала еду, то меняем рекорд и делаем новую еду, змейка уже увеличина
        if head.x == x_food and head.y == y_food: 
            record += 1 
            record_surface = update_record(record_surface, record)
            display.blit(record_surface, (0, 0))
            x_food, y_food = create_food(display)
        else: # если ничего не скушала, то нужно удалить хвост 
            tail = snake.pop()
            pygame.draw.rect(display, white, [tail.x, tail.y, SNAKE_SIZE, SNAKE_SIZE]) # заливаем область, откуда ушла змейка
       
        # рисуем красивую голову змеи 
        display.blit(snake_head, (head.x, head.y))
        if crash_flag == True and head != tail: 
            pygame.draw.rect(display, snake_lose_color, [head.x, head.y, SNAKE_SIZE, SNAKE_SIZE])
            game_over = True

        pygame.display.update()
