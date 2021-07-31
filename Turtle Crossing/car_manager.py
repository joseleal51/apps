from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.dist = STARTING_MOVE_DISTANCE

    pass

    def create_car(self):
        create = randint(1, 4)
        if create == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, randint(-240, 260))
            new_car.color(choice(COLORS))
            self.all_cars.append(new_car)
        else:
            pass

    def drive(self):
        for car in self.all_cars:
            car.forward(self.dist)

    def increase_difficulty(self):
        self.dist += MOVE_INCREMENT

    def new_level(self):
        self.all_cars = []
