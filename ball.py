from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("white")
        self.setheading(12)
        self.move_x = 10
        self.move_y = 10
        self.move()

    def move(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    def bounce(self):
        self.move_y = self.move_y * -1

    def bounce_1(self):
        self.move_x = self.move_x * -1
