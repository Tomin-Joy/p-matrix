import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 1920, 1080
FONT_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont("consolas", FONT_SIZE)

columns = WIDTH // FONT_SIZE
drops = [0] * columns

clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    for i in range(len(drops)):
        
        for offset in range(9):  
            char = random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            text = font.render(char, True, GREEN)
            y_position = (drops[i] - offset) * FONT_SIZE
            if y_position > 0:
                screen.blit(text, (i * FONT_SIZE, y_position))

        
        if drops[i] * FONT_SIZE > HEIGHT or random.random() > 0.98:  
            drops[i] = 0

        drops[i] += 1

    pygame.display.flip()
    clock.tick(13)
