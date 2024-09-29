from turtle import Screen
from ball import Ball
from paddleFile import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


right = Paddle((350, 0))
left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")
screen.onkey(left.go_up, "w")
screen.onkey(left.go_down, "s")


game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_posi()
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.reset_posi()
        scoreboard.rpoint()

screen.exitonclick()