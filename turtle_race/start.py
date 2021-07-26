from turtle import Turtle, Screen

tim = Turtle()
tom = Turtle()
tim.color("green")
tom.color("purple")

screen = Screen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.back(10)


def turn_clockwise():
    tim.left(30)


def turn_counter_clockwise():
    tim.right(30)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_clockwise)
screen.onkey(key="d", fun=turn_counter_clockwise)
screen.onkey(clear, "c")
screen.exitonclick()
