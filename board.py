from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.dot_line()
        self.score_sign()

    def dot_line(self):
        self.goto(0, 250)
        self.speed(0)
        self.setheading(270)
        while self.ycor() > -300:
            self.pensize(3)
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)

    def score_sign(self):
        self.goto(0, 265)
        self.write("SCORE", move=False, align="center", font=("Verdana", 20, "normal"))
