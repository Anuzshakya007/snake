import pygame
import time
import random

#initialize pygame
pygame.init()

# game window size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

#colors
WHITE = (255, 255, 255)
GREEN = (0, 255 ,0)
RED = (213,  50, 80)
BLUE = (50, 15, 213)
BLACK = (0, 0, 0)

# Game variables
speed = 5

#initialize window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock= pygame.time.Clock()

# snake and food
snake_pos = [[100,50], [90,50], [80,50]]
food_pos = [random.randrange(1,(WIDTH//CELL_SIZE)) * CELL_SIZE,
            random.randrange(1,(HEIGHT//CELL_SIZE)) * CELL_SIZE]
food_spawn = True

#snake movement
direction = 'RIGHT'
change_to = direction

#score
score = 0

# Font
font = pygame.font.SysFont("bahnschrift", 25)

#Function to display score
def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text,[10,10])

#Game over function
def gmae_over():
    screen.fill(BLACK)
    text = font.render("GAME OVER!!!", True, RED)
    screen.blit(text, [WIDTH//2 - 50, HEIGHT//2 - 10])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to= 'UP' 
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction!= 'RIGHT':
                change_to  = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    #Update direction
    direction = change_to

    #Move the snake
    if direction == 'UP':
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - CELL_SIZE])
    elif direction == 'DOWN':
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + CELL_SIZE])
    elif direction == 'LEFT':
        snake_pos.insert(0, [snake_pos[0][0] - CELL_SIZE, snake_pos[0][1]])
    elif direction == 'RIGHT':
        snake_pos.insert(0, [snake_pos[0][0] + CELL_SIZE, snake_pos[0][1]])
    
    ## Check if snake eats the food
    if abs(snake_pos[0][0] - food_pos[0]) < CELL_SIZE and abs(snake_pos[0][1] - food_pos[1]) < CELL_SIZE:
        score += 10
        food_spawn = False  # Generate new food
    else:
        snake_pos.pop()  # Remove the last segment (snake moves forward)

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//CELL_SIZE)) * CELL_SIZE,
                    random.randrange(1, (HEIGHT//CELL_SIZE)) * CELL_SIZE]
        food_spawn = True

    # Check for collisions (walls or itself)
    if (snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or
        snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0):
        gmae_over()
    
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            gmae_over()

    # Update screen
    screen.fill(BLACK)
    for segment in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
    
    show_score()
    pygame.display.update()
    
    # Control game speed
    clock.tick(speed)