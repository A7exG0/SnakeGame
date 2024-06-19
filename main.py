import pygame

pygame.init()
# Здесь делаем окно игры 
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake Game')

snake_color = (0,0,255)  # rgb(0,0,255)
background_color = (255, 255, 255) #rgb(255, 255, 255)
# Задаем начальные координаты змейки 
x1 = 250
y1 = 250
x1_change = 0
y1_change = 0

game_over = False 
clock = pygame.time.Clock()

while(not game_over):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y1_change = 10
                x1_change = 0

    x1 += x1_change 
    y1 += y1_change 

    clock.tick(10)
 
    display.fill(background_color)
    pygame.draw.rect(display, snake_color, [x1, y1, 20, 20])
    pygame.display.update()

pygame.quit()
quit()