import turtle
import random

#Part A:

screen = turtle.Screen()
turt1 = turtle.Turtle()
turt2 = turtle.Turtle()

turt1.speed(1)
turt2.speed(1)
turt1.penup()
turt2.penup()
turt1.goto(-100, 20)
turt2.goto(-100, -20)

turt1.forward(random.randrange(1, 101))
turt2.forward(random.randrange(1, 101))

turt1.goto(-100, 20)
turt2.goto(-100, -20)

for _ in range(10):
    turt1.forward(random.randrange(1, 11))
    turt2.forward(random.randrange(1, 11))

turt1.goto(-100, 20)
turt2.goto(-100, -20)

screen.exitonclick()

#Part B:
import math 
import pygame

pygame.init()
window = pygame.display.set_mode()

shape_sides = [3, 4, 6, 20, 100, 360]
running = True
window.fill("white")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                running = False

    mid_pos = 0
    for n in range(len(shape_sides)):
        mid_pos += 100
        num_of_sides = shape_sides[n]
        angle = 360/num_of_sides
        points = []
        for i in range(shape_sides[n]):
            point = []
            radians = math.radians(angle*i)
            x = 100 + 50 * math.cos(radians)
            y = mid_pos + 50 * math.sin(radians)
            point.append(x)
            point.append(y)
            points.append(point)
        pygame.draw.polygon(window, "blue", points)
        print(points)
        pygame.time.wait(1000)
        pygame.display.flip()
        window.fill("white")
