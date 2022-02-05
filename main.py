from turtle import Turtle, Screen
import random

timmy = [Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle"), Turtle(shape="turtle"),
         Turtle(shape="turtle"), Turtle(shape="turtle")]
race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Make your Bet: ")
colors = ["red", "orange", "purple", "yellow", "green", "blue"]

x = -240
y = -150
for t in range(0, 6):
    timmy[t].penup()
    timmy[t].color(colors[t])
    timmy[t].goto(x, y)
    y += 50

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in timmy:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} is the Winner")
            else:
                print(f"You Lost! {winning_color} is the Winner!")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()
