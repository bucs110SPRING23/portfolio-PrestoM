import pygame
import random
import math

pygame.init()
window = pygame.display.set_mode((640, 640))
running = True
screen_w = pygame.display.get_window_size()[0]
screen_h = pygame.display.get_window_size()[1]
window.fill("blue")

dart_coords_1 = []
dart_coords_2 = []
center = [screen_w/2, screen_h/2]
rounds = 10
red_hit = 0
blue_hit = 0

bet_made = False
bet = None

rect_1 = pygame.Rect(center[0]-center[0]/2, center[1]-center[1]/2, 60, 60)
rect_2 = pygame.Rect(center[0]+center[0]/2, center[1]-center[1]/2, 60, 60)

for i in range(rounds):
    dart_x_1 = random.randrange(0, screen_w+1)
    dart_x_2 = random.randrange(0, screen_w+1)
    dart_y_1 = random.randrange(0, screen_h+1)
    dart_y_2 = random.randrange(0, screen_h+1)
    center_dist_1 = math.hypot(center[0]-dart_x_1, center[1]-dart_y_1)
    center_dist_2 = math.hypot(center[0]-dart_x_2, center[1]-dart_y_2)
    if (center_dist_1 > screen_w/2):
        dart_coords_1.append([dart_x_1, dart_y_1, False])
    else:
        dart_coords_1.append([dart_x_1, dart_y_1, True])

    if (center_dist_2 > screen_w/2):
        dart_coords_2.append([dart_x_2, dart_y_2, False])
    else:
        dart_coords_2.append([dart_x_2, dart_y_2, True])


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if rect_1.collidepoint(pos): 
                bet_made = True 
                bet = "1"
            elif rect_2.collidepoint(pos):
                bet_made = True
                bet = "2"

    pygame.draw.circle(window, "pink", [screen_w/2, screen_h/2], screen_w//2, screen_h//2, 0)
    pygame.draw.line(window, "black", [screen_w/2, 0], [screen_w/2, screen_h/2])
    pygame.draw.line(window, "black", [screen_w/2, screen_h], [screen_w/2, screen_h/2])
    pygame.draw.line(window, "black", [screen_w, screen_h/2], [screen_w/2, screen_h/2])
    pygame.draw.line(window, "black", [0, screen_h/2], [screen_w/2, screen_h/2])

#ADD EVENT FOR CLICKING
    if not bet_made:
        pygame.draw.rect(window, "red", rect_1)
        pygame.draw.rect(window, "blue", rect_2)

    if bet_made:
        for coord in range(len(dart_coords_1)):
            if dart_coords_1[coord][2]:
                pygame.draw.circle(window, (255,0,0), [dart_coords_1[coord][0], dart_coords_1[coord][1]], 5, 0)
                red_hit += 1
            else:
                pygame.draw.circle(window, (255,120,60), [dart_coords_1[coord][0], dart_coords_1[coord][1]], 5, 0)

            if dart_coords_2[coord][2]:
                pygame.draw.circle(window, (0,0,255), [dart_coords_2[coord][0], dart_coords_2[coord][1]], 5, 0)
                blue_hit += 1
            else:
                pygame.draw.circle(window, (20,200,255), [dart_coords_2[coord][0], dart_coords_2[coord][1]], 5, 0)

        font = pygame.font.Font(None, 48)
        if red_hit > blue_hit:
            text = font.render(f"Player 1 (red) Won!", True, "white")
            window.blit(text, (center[0]-center[0]/2, center[1]))
            if bet == "1":
                text2 = font.render(f"Your bet for Player {bet} was correct!", True, "white")
                window.blit(text2, (center[0]-center[0]/1.2, center[1] + 100))
            elif bet == "2":
                text2 = font.render(f"Your bet for Player {bet} was incorrect!", True, "white")
                window.blit(text2, (center[0]-center[0]/1.2, center[1] + 100))
        elif blue_hit > red_hit:
            text = font.render(f"Player 2 (blue) Won!", True, "white")
            window.blit(text, (center[0]-center[0]/2, center[1]))
            if bet == "1":
                text2 = font.render(f"Your bet for Player {bet} was incorrect!", True, "white")
                window.blit(text2, (center[0]-center[0]/1.2, center[1] + 100))
            elif bet == "2":
                text2 = font.render(f"Your bet for Player {bet} was correct!", True, "white")
                window.blit(text2, (center[0]-center[0]/1.2, center[1] + 100))
        else: 
            text = font.render(f"It's a tie!", True, "white")
            window.blit(text, (center[0]-center[0]/4, center[1]))
       

    pygame.display.flip()