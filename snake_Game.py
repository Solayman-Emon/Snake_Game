'''

Authors ::  Solayman Hossain Emon

Aust CSE 37th Batch

'''

import turtle
import time

delay = 0.2

# Set up the Screen
wn = turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("yellow")
wn.setup(height=600, width=800)
wn.tracer(0)

# Snake Food

snk_food = turtle.Turtle()
snk_food.shape("circle")
snk_food.color("red")
snk_food.penup()
snk_food.goto(0, 100)

# Snake Head
snk_head = turtle.Turtle()
snk_head.speed(0)
snk_head.shape("square")
snk_head.color("black")
snk_head.penup()
snk_head.goto(0, 0)
snk_head.direction = "stop"


def move():
    if snk_head.direction == "up":
        y = snk_head.ycor()
        snk_head.sety(y + 20)

    elif snk_head.direction == "down":
        y = snk_head.ycor()
        snk_head.sety(y - 20)

    elif snk_head.direction == "right":
        x = snk_head.xcor()
        snk_head.setx(x + 20)

    elif snk_head.direction == "left":
        x = snk_head.xcor()
        snk_head.setx(x - 20)


def go_up():
    snk_head.direction = "up"


def go_down():
    snk_head.direction = "down"


def go_right():
    snk_head.direction = "right"


def go_left():
    snk_head.direction = "left"

# Keyboard Key
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

# Main Loop
while True:
    wn.update()
    move()
    time.sleep(delay)

# Keep the window open
wn.mainloop()
