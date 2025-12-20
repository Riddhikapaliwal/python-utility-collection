import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncy Ball Animation")

# Ball properties
x = WIDTH // 2
y = HEIGHT // 2
radius = 25
speed_x = 5
speed_y = 4
color = (255, 0, 0)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    x += speed_x
    y += speed_y

    # Bounce logic
    if x - radius <= 0 or x + radius >= WIDTH:
        speed_x *= -1
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    if y - radius <= 0 or y + radius >= HEIGHT:
        speed_y *= -1
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Draw
    screen.fill((0, 0, 0))  # black background
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.update()

    clock.tick(60)  # 60 FPS

pygame.quit()
