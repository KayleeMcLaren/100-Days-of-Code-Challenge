
import turtle
import pandas

"""Set up the screen and map image"""
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

"""Checks if the user's answer is correct and then updates the display accordingly to show how many states have been guessed correctly. The name of the state 
then also appears on the image of the map of the U.S. If "Exit" is entered, then the program ends and a list of all the missed states is created. If all 50 states
are guessed correctly, the program ends"""
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name: ").title()
    if answer_state == "Exit":
        missed_states = [state_name for state_name in all_states if state_name not in guessed_states]
        pandas.DataFrame(missed_states).to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        
