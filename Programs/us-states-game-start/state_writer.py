from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")


class StateWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def print(self, text, x, y):
        self.setposition(x, y)
        self.write(text, align=ALIGNMENT, font=FONT)