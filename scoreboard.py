from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_board()

    def score_board(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.score}", align="center", font=(FONT))

    def update_score_board(self):
        self.score += 1
        self.score_board()

    def reset_score_board(self):
        self.score = 0
        self.score_board()
