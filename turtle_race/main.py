from turtle import Turtle, Screen
import random


race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    y = -150 + i*50
    new_turtle.goto(x=-220, y=y)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)


if user_bet:
    race = True

while race:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
