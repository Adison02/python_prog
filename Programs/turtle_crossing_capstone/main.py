from turtle import Screen
from player import Player
from car_manager import CarManager
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

for i in range(0, 21):
    car_manager.spawn_car()

game_is_on = True
while(game_is_on):
    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()