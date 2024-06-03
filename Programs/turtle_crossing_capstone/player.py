from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.set_up()

    def set_up(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setposition(0, new_y)
