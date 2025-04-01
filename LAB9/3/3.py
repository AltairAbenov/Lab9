import pygame
import math

pygame.init()
pygame.display.set_caption("Paint")

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

# Initial settings
color = BLACK
brush_size = 5
shape_size = 50
drawing = False
tool = "brush"
start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if tool == "rect":
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], shape_size, shape_size), 2)
            elif tool == "circle":
                pygame.draw.circle(screen, color, start_pos, shape_size, 2)
            elif tool == "square":
                # Draw a square
                pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], shape_size, shape_size), 2)
            elif tool == "right_triangle":
                # Draw a right triangle
                pygame.draw.polygon(screen, color, [
                    start_pos,
                    (start_pos[0] + shape_size, start_pos[1]),
                    (start_pos[0], start_pos[1] + shape_size)
                ], 2)
            elif tool == "equilateral_triangle":
                # Draw an equilateral triangle
                height = shape_size * math.sqrt(3) / 2
                pygame.draw.polygon(screen, color, [
                    start_pos,
                    (start_pos[0] + shape_size, start_pos[1]),
                    (start_pos[0] + shape_size/2, start_pos[1] - height)
                ], 2)
            elif tool == "rhombus":
                # Draw a rhombus
                pygame.draw.polygon(screen, color, [
                    (start_pos[0], start_pos[1] - shape_size),
                    (start_pos[0] + shape_size, start_pos[1]),
                    (start_pos[0], start_pos[1] + shape_size),
                    (start_pos[0] - shape_size, start_pos[1])
                ], 2)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(screen, color, event.pos, brush_size)
            elif tool == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)

        # Change tools or adjust settings
        elif event.type == pygame.KEYDOWN:
            # Tool selection
            if event.key == pygame.K_q:
                tool = "brush"
            elif event.key == pygame.K_w:
                tool = "rect"
            elif event.key == pygame.K_e:
                tool = "circle"
            elif event.key == pygame.K_r:
                tool = "eraser"
            elif event.key == pygame.K_y:
                tool = "square"
            elif event.key == pygame.K_u:
                tool = "right_triangle"
            elif event.key == pygame.K_i:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_o:
                tool = "rhombus"
            # Color selection
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE
            elif event.key == pygame.K_4:
                color = BLACK
            elif event.key == pygame.K_5:
                color = WHITE
            # Adjust shape size
            elif event.key == pygame.K_6:
                shape_size += 5
            elif event.key == pygame.K_7:
                shape_size = max(5, shape_size - 5)

    pygame.display.flip()

pygame.quit()
