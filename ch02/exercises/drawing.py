import turtle

num_sides = int(input("Enter number of sides: "))
len_sides = float(input("Enter length of each side: "))

turt = turtle.Turtle()
turt.color("blue")

degs = 360 / num_sides

for i in range(num_sides):
    turt.forward(len_sides)
    turt.left(degs)

turtle.exitonclick()