from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.refresh()

    def refresh(self):
        self.clear()
        self.setposition(-50, 220)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.setposition(50, 220)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_add_point(self):
        self.l_score += 1
        self.refresh()

    def r_add_point(self):
        self.r_score += 1
        self.refresh()
