#the left direction for the wave (one part of the wave)
def wave_left(distance, angle, sides, turtle):
    for i in range(sides):
        turtle.forward(distance)
        turtle.left(angle)

#right direction for the wave (other part of the wave)
def wave_right(distance, angle, sides, turtle):
    for i in range(sides):
        turtle.forward(distance)
        turtle.right(angle)

#combines the two functions above to form one cohesive wave
def wave(rang, t, d, a):
    for i in range(rang):
        wave_left(d, a, 100, t)
        t.forward(30)
        wave_right(d, a, 100, t)
        t.forward(40)
