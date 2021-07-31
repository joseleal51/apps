from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.score = 0
        self.update_scoreboard()

    def increase_level(self):
        self.score += 1
        self.level += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER\nSCORE: {self.score}", align="center", font=FONT)
