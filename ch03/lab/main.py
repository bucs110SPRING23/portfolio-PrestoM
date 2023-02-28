import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((640, 640))
running = True
screen_w = pygame.display.get_window_size()[0]
screen_h = pygame.display.get_window_size()[1]
window.fill("blue")

dart_coords = []
center = [screen_w/2, screen_h/2]

for i in range(10):
    dart_x = random.randrange(0, screen_w+1)
    dart_y = random.randrange(0, screen_h+1)
    center_dist = math.hypot(center[0]-dart_x, center[1]-dart_y)
    if center_dist > screen_w/2:
        dart_coords.append([dart_x, dart_y, False])
    else:
        dart_coords.append([dart_x, dart_y, True])

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(window, "pink", [screen_w/2, screen_h/2], screen_w//2, screen_h//2, 0)
    pygame.draw.line(window, "black", [screen_w/2, 0], [screen_w/2, screen_h/2])
    pygame.draw.line(window, "black", [screen_w/2, screen_h], [screen_w/2, screen_h/2])
    pygame.draw.line(window, "black", [screen_w, screen_h/2], [screen_w/2, screen_h/2])
    pygame.draw.line(window, "black", [0, screen_h/2], [screen_w/2, screen_h/2])

    for coord in dart_coords:
        if coord[2]:
            pygame.draw.circle(window, "black", [coord[0], coord[1]], 5, 0)
        else:
            pygame.draw.circle(window, "red", [coord[0], coord[1]], 5, 0)

    pygame.display.flip()