from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car = Turtle()
        car.color(choice(COLORS))
        car.shape("square")
        car.penup()
        car.shapesize(stretch_len=2)
        car.setheading(180)
        car.setposition(self.generate_position())
        # APPENDING NEW CAR
        self.cars.append(car)

    def generate_position(self):
        new_x = randint(320, 1500)
        new_y = randint(-200, 200)
        return (new_x, new_y)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -320:
                car.setposition(self.generate_position())
            car.forward(self.move_distance)