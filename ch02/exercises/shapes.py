import pygame

pygame.init()
window = pygame.display.set_mode((640, 400))
running = True
window.fill((0,0,0))

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(window, "white", [320,300], 75, 0)
    pygame.draw.circle(window, "white", [320, 205], 55, 0)
    pygame.draw.circle(window, "white", [320,145], 35, 0)
    pygame.display.flip()
 