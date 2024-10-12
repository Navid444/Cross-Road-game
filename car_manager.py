from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FONT = ("Courier", 24, "bold")


class CarManager(Turtle):

    def __init__(self):

        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1, 8)
        if random_chance == 4:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 4

    def reset_level_up(self):
        self.car_speed = MOVE_INCREMENT
