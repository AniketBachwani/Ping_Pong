from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color("white")
        self.score_1()
        self.score_2()

    def score_1(self, score=0):
        self.goto(-60, 230)
        self.write(f"{score}", move=False, align="center", font=("Verdana", 20, "normal"))

    def score_2(self, score=0):
        self.goto(60, 230)
        self.write(f"{score}", move=False, align="center", font=("Verdana", 20, "normal"))
