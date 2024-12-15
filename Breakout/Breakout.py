import turtle
import random

# Screen setup
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle setup
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball setup
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Initial ball speed
ball.dy = -0.15

# Score setup
score = 0
lives = 3
level = 1

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}  Lives: {lives}  Level: {level}", align="center", font=("Courier", 16, "normal"))

# Brick setup
def create_bricks():
    global bricks
    bricks = []
    brick_colors = ["red", "green", "blue", "yellow"]
    for row in range(level + 3):  # Increase the number of rows with level
        for col in range(8):
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape("square")
            brick.color(brick_colors[row % len(brick_colors)])
            brick.penup()
            brick.goto(-350 + (col * 80), 250 - (row * 30))
            bricks.append(brick)

create_bricks()

# Functions to control the paddle
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Update score and lives display
def update_scoreboard():
    score_display.clear()
    score_display.write(f"Score: {score}  Lives: {lives}  Level: {level}", align="center", font=("Courier", 16, "normal"))

# Function to increase ball speed
def increase_ball_speed():
    ball.dx *= 1.1
    ball.dy *= 1.1

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        lives -= 1
        ball.goto(0, 0)
        ball.dx = 0.15  # Reset ball speed
        ball.dy = -0.15
        if lives == 0:
            # Game over
            win.clear()
            win.bgcolor("black")
            game_over_display = turtle.Turtle()
            game_over_display.color("white")
            game_over_display.penup()
            game_over_display.hideturtle()
            game_over_display.goto(0, 0)
            game_over_display.write("Game Over! Press 'q' to quit.", align="center", font=("Courier", 24, "bold"))
            win.update()
            win.listen()
            win.onkeypress(win.bye, "q")
            break

    # Paddle and ball collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Ball and bricks collision
    for brick in bricks:
        if (ball.ycor() > brick.ycor() - 10 and ball.ycor() < brick.ycor() + 10) and (ball.xcor() > brick.xcor() - 40 and ball.xcor() < brick.xcor() + 40):
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            score += 10
            update_scoreboard()
            break

    # Level up condition
    if not bricks:
        level += 1
        score += 100
        update_scoreboard()
        create_bricks()  # Create new bricks for the next level
        increase_ball_speed()  # Increase the ball speed for the next level
