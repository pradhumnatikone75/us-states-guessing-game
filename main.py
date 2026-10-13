import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tom= turtle.Turtle()
tom.hideturtle()
tom.penup()

data = pandas.read_csv("50_states.csv")
state_name=data["state"]

guessed_state=[]

right_guess_count=0
game_is_on=True
while game_is_on:
    user_guess_state=turtle.textinput(title=f"{right_guess_count}/50 State Correct", prompt="Enter next state name ")
    proper_user_guess_state=user_guess_state.title()
    if user_guess_state == "q":
        game_is_on=False

    x_axis_state=0
    y_axis_state=0
    for state in state_name:
        if proper_user_guess_state == state:
            if proper_user_guess_state not in guessed_state:
                guessed_state.append(state)
                right_guess_count+=1


                x_axis_state=int(data[data["state"] == proper_user_guess_state]["x"].item())
                y_axis_state=int(data[data["state"] == proper_user_guess_state]["y"].iloc[0])

                tom.goto(x_axis_state,y_axis_state)
                tom.write(proper_user_guess_state)
    if right_guess_count>=50:
        game_is_on=False

#New CSV file for state name which not answered by user not use in proper codeflow just to skill check
remaining_state=[state for state in state_name if state not in guessed_state]
ds=pandas.Series(remaining_state)
ds.to_csv("state_to_learn.csv")