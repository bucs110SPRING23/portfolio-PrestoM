import turtle
from waves import *
bob = turtle.Turtle()
window = turtle.Screen()
turtle.colormode(255)
bob.pensize(50)
turtle.tracer(False)

w_angle = 400 / 360

#1800
def gen_waves():
    #red value
    r = 0
    #green value
    g = 0
    #blue value
    b = 0
    for i in range(119):
        #wave
        wave(10, bob, 1, w_angle)
        #increments the value of red
        r += 10
        if (r >= 255):
            r = r - 255
        #increments the value of green
        g += 20
        if (g >= 255):
            g = g - 255
        #increments the value of blue
        b += 30
        if (b >= 255):
            b = b - 255

        #reset the position of the turtle (bob)
        bob.penup()
        bob.goto(0, 0)
        bob.pendown()
        #turns the turtle by small amounts after each wave is formed
        bob.right(3)
        bob.color(r, g, b)

def main():
    gen_waves()
    window.exitonclick()

main()

