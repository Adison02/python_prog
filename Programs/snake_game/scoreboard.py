from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.set_settings()
        self.refresh()

    def set_settings(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def refresh(self):
        self.clear()
        text = f"Score: {self.score}"
        self.write(text, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0, 0)
        text = f"GAME OVER"
        self.write(text, align=ALIGNMENT, font=FONT)