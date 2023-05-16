import pygame

def threenp1(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count += 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit+1):
        objs_in_sequence[i] = threenp1(i)
    return objs_in_sequence

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    window = pygame.display.set_mode((640, 640))
    running = True
    window.fill("white")
    iters = list(threenplus1_iters_dict.items())
    scaled_iters = []
    for i in iters:
        scaled_iters.append((i[0]*20, i[1]*20))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        new_display = pygame.transform.flip(window, False, True)
        width, height = new_display.get_size()
        window.blit(new_display, (0, 0))
        pygame.display.flip()
        window.fill("white")
        pygame.draw.lines(window, "black", True, scaled_iters)
        

def main():
    upper = 20
    rang = threenp1range(upper)
    maxes = []
    for i in range(2,upper+1):
        maxes.append(rang[i])
    max_so_far = max(maxes)
    for i in range(2,upper+1):
        if rang[i] == max_so_far:
            print(f"Max so Far: {i} : {max_so_far}")
        
    graph_coordinates(threenp1range(upper))

main()