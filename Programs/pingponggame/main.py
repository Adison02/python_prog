from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.game_speed)
    screen.update()
    ball.move()

    # DETECT BALL COLLISION WITH WALL
    if ball.ycor() > 285 or ball.ycor() < -285:
        print("collision with wall")
        ball.bounce_y()

    # DETECT BALL COLLISION WITH PADDLES
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.i_game_speed()

    # DETECT L PADDLE MISSES
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_add_point()

    # DETECT R PADDLE MISSES
    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.l_add_point()

screen.exitonclick()
