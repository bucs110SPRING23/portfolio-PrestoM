import turtle
import random

turt = turtle.Turtle()
scr = turtle.Screen()
scr.setup(600, 600)
print(scr.window_width())
print(scr.window_height())


screenOff = False
while not screenOff: 
    num = random.randint(1,2)
    if num == 1:
        turt.right(90)
    elif num == 2: 
        turt.left(90)
    turt.forward(50)
    print(turt.pos())
    if (turt.pos()[0] > scr.window_width()/2) or (turt.pos()[0] < (-1*(scr.window_width()/2))) or (turt.pos()[1] > scr.window_height()/2) or (turt.pos()[1] < (-1*(scr.window_height()/2))):
        screenOff = True

turtle.exitonclick()


