import turtle as t
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = t.Turtle()
t.colormode(255)

tim.pensize(1)
tim.speed("fastest")

tim.setheading(0)
heading = 0
step = 20
for _ in range(int(365/step)):
    heading += step
    tim.setheading(heading)
    tim.color(random_color())
    tim.circle(100)



screen = t.Screen()
screen.exitonclick()