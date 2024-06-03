from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

t_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

offset_y = 25
for i in range(0, len(t_colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(t_colors[i])
    new_turtle.penup()
    new_turtle.goto(-200, 400 / -len(t_colors) + offset_y * i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print("YOU WIN")
            else:
                print("YOU LOSE")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()