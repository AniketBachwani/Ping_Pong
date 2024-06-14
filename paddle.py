from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.up()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(1, 5)
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 240:
            self.setheading(90)
            self.forward(40)
        else:
            pass

    def move_down(self):
        if self.ycor() > -240:
            self.setheading(270)
            self.forward(40)
        else:
            pass
