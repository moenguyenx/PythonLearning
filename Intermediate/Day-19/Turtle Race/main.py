import random as r
from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color").lower()

color = ["red", "orange", "blue", "green", "pink", "black"]
y_pos = [-150, -100, -50, 50, 100, 150]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-300, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The winner is the {winner} turtle.")
            else:
                print(f"You've lost! The winner is the {winner} turtle")
        turtle.forward(r.randint(0, 20))

screen.exitonclick()
