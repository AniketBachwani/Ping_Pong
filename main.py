from paddle import Paddle
from board import Board
from ball import Ball
from score import Score
from turtle import Screen
import time

screen = Screen()
screen.setup(1200, 600)
screen.bgcolor("black")
screen.title("pong game")
screen.tracer(0)

board_1 = Board()
paddle_1 = Paddle(570, 0)
paddle_2 = Paddle(-570, 0)
ball_1 = Ball()
score_0 = Score()

screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

score_1 = 0
score_2 = 0
game_on = True
while game_on:
    x_1 = paddle_1.xcor()
    y_1 = paddle_1.ycor()
    x_2 = paddle_2.xcor()
    y_2 = paddle_2.ycor()
    ball_1.move()
    time.sleep(0.025)
    screen.update()
    if -610 > ball_1.xcor():
        board_1.__init__()
        ball_1.__init__()
        score_2 += 1
        score_0.clear()
        score_0.score_1(score_1)
        score_0.score_2(score_2)
    if 600 < ball_1.xcor():
        board_1.__init__()
        ball_1.__init__()
        score_1 += 1
        score_0.clear()
        score_0.score_2(score_2)
        score_0.score_1(score_1)
    if 555 < ball_1.xcor() >= 550 and paddle_1.distance(ball_1) < 50:
        ball_1.bounce_1()
    if -555 > ball_1.xcor() <= -550 and paddle_2.distance(ball_1) < 50:
        ball_1.bounce_1()
    if ball_1.ycor() > 290 or ball_1.ycor() < -290:
        ball_1.bounce()
