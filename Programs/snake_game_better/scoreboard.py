from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.set_settings()
        self.refresh()

    def set_settings(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)

    def refresh(self):
        self.clear()
        text = f"Score: {self.score} High Score: {self.high_score}"
        self.write(text, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.update_high_score()
        self.score = 0
        self.refresh()

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    def add_point(self):
        self.score += 1
        self.refresh()
