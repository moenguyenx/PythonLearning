import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(800, 600)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

score = 0
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) <= 50:
    answer_state = screen.textinput(prompt="What's another state name?",
                                    title=f"{len(guessed_state)}/50 state guessed").title()
    if answer_state == "Exit":
        state_to_learn = [state for state in all_states if state not in guessed_state]

        series_to_learn = pd.DataFrame(state_to_learn)
        series_to_learn.to_csv("learning.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # access the row to get x and y value
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# state to learn.csv
