import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Ablak létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Feed the dog")

# Színek
BLACK = (0, 0, 0)

# Időzítő
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fekete háttér kirajzolása
    screen.fill(BLACK)

    # Frissítés
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
