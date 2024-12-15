from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((360,0))
l_paddle = Paddle((-370,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect r_paddle misses
    if ball.xcor() > 380:
        ball.original_position()
        scoreboard.l_point()
    
    #Detect l_paddle misses
    if ball.xcor() < -380:
        ball.original_position()
        scoreboard.r_point()


screen.exitonclick()