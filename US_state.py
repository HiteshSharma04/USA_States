from turtle import Turtle, Screen
import pandas as pd

img = "projects/pandas/blank_states_img.gif"
screen = Screen()
screen.title("US States Game")
screen.addshape(img)
t = Turtle(img)

data = pd.read_csv("projects/pandas/50_states.csv")
all = data.state.to_list()
# print(all)

# print(user)
guess = []

while len(guess) < 50:
    user = screen.textinput(title=f"{len(guess)}/50 Guess State" , prompt="What's the State's Names?").title()

    if user == "Exit":
        miss = []
        for i in all:
            if i not in guess:
                miss.append(i)
        learn = pd.DataFrame(miss)
        learn.to_csv("projects/pandas/learn.csv")
        break
    if user in all:
        guess.append(user)
        h = Turtle()
        h.hideturtle()
        h.penup()
        state = data[data.state == user]
        h.goto(state.x.item() , state.y.item())
        h.write(user)


