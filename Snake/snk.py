import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
SNAKE_COLOR = (0, 128, 0)
FOOD_COLOR = (255, 0, 0)
background_color= (0, 0, 0)
SPEED = 5

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, -1)  # Initial direction (up)
snake_speed = SPEED
score = 0

def change_colors():
    global background_color, snake_color, food_color
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    snake_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    food_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Food variables
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
            elif event.key == pygame.K_SPACE:
                change_colors()

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Check for collisions
    if new_head == food:
        score += 1
        snake_speed += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check for game over
    if (
        new_head in snake
        or new_head[0] < 0
        or new_head[0] >= GRID_WIDTH
        or new_head[1] < 0
        or new_head[1] >= GRID_HEIGHT
    ):
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Draw the background
    screen.fill(background_color)
    # Draw the food
    pygame.draw.rect(
        screen,
        FOOD_COLOR,
        (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
    )

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen,
            SNAKE_COLOR,
            (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
        )

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control the snake speed
    pygame.time.delay(1000 // snake_speed)
