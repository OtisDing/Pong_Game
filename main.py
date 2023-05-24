from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rPaddle = Paddle((350, 0))
lPaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(rPaddle.goUp, "Up")
screen.onkey(rPaddle.goDown, "Down")
screen.onkey(lPaddle.goUp, "w")
screen.onkey(lPaddle.goDown, "s")

gameIsOn = True

while gameIsOn:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    #Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    #Detecting collision with right paddle
    if ball.distance(rPaddle) < 50 and ball.xcor() > 320 or ball.distance(lPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    #Detecting when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.lPoint()

    #Detecting when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rPoint()


screen.exitonclick()
