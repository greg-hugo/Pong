import turtle
import random
import time
import os
import sys

# Screen
win = turtle.Screen()
win.title("Pong - Gregory Hugo")
win.colormode(255)
win.bgcolor(104, 83, 105)
win.setup(width=900, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color(198, 216, 175)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color(198, 216, 175)
paddle_b.penup()
paddle_b.goto(400, 0)

# Pong Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(198, 216, 175)
ball.penup()
ball.goto(0, 0)

direction_x = random.randrange(-1, 2, 2)
direction_y = random.randrange(-1, 2, 2)

ball.dx = 0.4 * direction_x
ball.dy = 0.4 * direction_y

# Pen - Score
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color(198, 216, 175)
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: {} | Player B: {}".format(score_a, score_b),
          align="center", font=("Poppins", 16, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    if y >= 250:
        paddle_a.sety(250)
    else:
        y += 25
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y <= -235:
        paddle_a.sety(-240)
    else:
        y -= 25
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y >= 250:
        paddle_b.sety(250)
    else:
        y += 25
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y <= -235:
        paddle_b.sety(-240)
    else:
        y -= 25
        paddle_b.sety(y)


def write_score():
    pen.write("Player A: {} | Player B: {}".format(score_a, score_b),
              align="center", font=("Poppins", 16, "normal"))


def decide_victory():
    winner = turtle.Turtle()
    winner.speed(0)
    winner.color(198, 216, 175)
    winner.penup()
    winner.hideturtle()
    winner.goto(0, 0)
    if score_a == 10:
        winner.write("Player A WINS!!!",
                     align="center", font=("Poppins", 24, "normal"))
    if score_b == 10:
        winner.write("Player B WINS!!!",
                     align="center", font=("Poppins", 24, "normal"))
    winner.goto(0, -50)
    winner.write("-- Click anywhere to replay --",
                 align="center", font=("Poppins", 15, "normal"))


def restart_game(x, y):
    os.execl(sys.executable, sys.executable, *sys.argv)


# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Randomize up or down motion of ball
    direction_y = random.randrange(-1, 2, 2)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle - Ball Collision
    if 390 > ball.xcor() > 380 \
            and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(380)
        ball.dx *= -1

    if -390 < ball.xcor() < -380 \
            and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-380)
        ball.dx *= -1

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 440:
        score_a += 1
        ball.goto(0, 0)
        ball.dy *= direction_y
        ball.dx *= -1
        pen.clear()
        write_score()
        time.sleep(1)
    elif ball.xcor() < -440:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= direction_y
        pen.clear()
        write_score()
        time.sleep(1)

    if score_a == 10 or score_b == 10:
        win.resetscreen()
        break

while True:
    decide_victory()
    win.onscreenclick(restart_game, 1)
