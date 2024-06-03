import turtle as turtle_module

turtle = turtle_module.Turtle()
screen = turtle_module.Screen()


def forward():
    turtle.forward(5)

def back():
    turtle.backward(5)

def left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def make_dot():
    turtle.dot(50)

screen.listen()
screen.onkey(forward, "Up")
screen.onkey(back, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(make_dot, "space")


screen.exitonclick()
