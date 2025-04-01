import pygame
import random

# Initialize pygame
pygame.init()
pygame.display.set_caption("Game")

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_small = pygame.font.SysFont("Verdana", 20)
score = 0
level = 1

# Initial snake parameters
snake = [(100, 100)]
SPEED = 12
direction = (CELL_SIZE, 0)

# Food attributes
food_types = [
    {'color': RED, 'points': 1, 'lifetime': 7000},
    {'color': GREEN, 'points': 2, 'lifetime': 9000},
    {'color': BLUE, 'points': 3, 'lifetime': 10000}
]

def generate_food():
    return {
        'pos': (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE),
        **random.choice(food_types),
        'spawn_time': pygame.time.get_ticks()
    }

food = generate_food()
running = True

while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    # Update snake position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        running = False  # Game over
    else:
        snake.insert(0, new_head)
        
        if new_head == food['pos']:
            score += food['points']
            food = generate_food()

            # Level up every 3 points
            if score % 3 == 0:
                level += 1
                SPEED += 2  
        else:
            snake.pop()
    
    # Check food expiration
    if pygame.time.get_ticks() - food['spawn_time'] > food['lifetime']:
        food = generate_food()
    
    # Draw snake and food
    for segment in snake:
        pygame.draw.rect(screen, BLACK, (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, food['color'], (*food['pos'], CELL_SIZE, CELL_SIZE))

    # Display score and level
    screen.blit(font_small.render(f"Points: {score}", True, BLACK), (10, 10))
    screen.blit(font_small.render(f"Level: {level}", True, BLACK), (10, 30))

    pygame.display.flip()
    clock.tick(SPEED)  # Controls game speed properly

pygame.quit()