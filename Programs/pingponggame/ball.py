from turtle import Turtle
GAME_SPEED = 0.07

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.game_speed = GAME_SPEED
        self.set_up()

    def set_up(self):
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        # SETTING POSITION
        self.setposition(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def i_game_speed(self):
        if self.game_speed > 0.025:
            self.game_speed -= 0.005

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.setposition(0, 0)
        self.bounce_x()
