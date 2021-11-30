
import turtle as t


window = t.Screen()
window.title("Bing Bong")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

ball=t.Turtle()
ball.speed()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

score1 = 0
score2 = 0
score = t.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0   Player2: 0", align="center", font=("Courier", 24, "normal"))

def leftpaddle_up():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)

def leftpaddle_down():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)

def rightpaddle_up():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)
def rightpaddle_down():
    y = rightpaddle.ycor()
    y -= 20
    rightpaddle.sety(y)

window.listen()
window.onkeypress(leftpaddle_up, "w")
window.onkeypress(leftpaddle_down, "s")
window.onkeypress(rightpaddle_up, "Up")
window.onkeypress(rightpaddle_down, "Down")
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player1: {}  Player2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player1: {}  Player2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() -40:
        ball.setx(340)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() -40:
        ball.setx(-340)
        ball.dx *= -1