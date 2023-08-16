import pygame
import sys
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("지렁이 게임")


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


worm_size = 20
worm_pos = [[100, 100]]
worm_speed = 20
dx, dy = 0, 0


food_pos = [random.randrange(0, WIDTH-worm_size, 20), random.randrange(0, HEIGHT-worm_size, 20)]
food_spawn = True


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -worm_speed
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, worm_speed
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -worm_speed, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = worm_speed, 0

    new_pos = [worm_pos[-1][0] + dx, worm_pos[-1][1] + dy]
    worm_pos.append(new_pos)

    
    if new_pos == food_pos:
        food_spawn = False
    else:
        worm_pos.pop(0)

    if not food_spawn:
        food_pos = [random.randrange(0, WIDTH - worm_size, 20), random.randrange(0, HEIGHT - worm_size, 20)]
        food_spawn = True

   
    win.fill(WHITE)
    for pos in worm_pos:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], worm_size, worm_size))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], worm_size, worm_size))

    pygame.display.flip()

    
    if new_pos[0] < 0 or new_pos[0] > WIDTH - worm_size or new_pos[1] < 0 or new_pos[1] > HEIGHT - worm_size:
        pygame.quit()
        sys.exit()


    if len(worm_pos) > 1 and new_pos in worm_pos[:-1]:
        pygame.quit()
        sys.exit()

    clock.tick(10)

	
