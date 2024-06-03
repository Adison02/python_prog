import time, turtle, pandas
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_writer = StateWriter()

states_df = pandas.read_csv("50_states.csv")

while len(states_df) != 0:
    print("----------------Number of guessed states: ", len(states_df))
    # USER INPUT
    answer_input = screen.textinput(title="Guess the State", prompt="What's another state? \n(type 'leave' to exit).")
    if answer_input == "leave":
        screen.bye()

    # GETTING STATE
    user_state = states_df[states_df["state"] == answer_input]
    if not user_state.empty:
        name = answer_input
        x = int(user_state.x)
        y = int(user_state.y)

        state_writer.print(name, x, y)
        states_df = states_df.drop(user_state.index)
    else:
        print("Not found ", answer_input, ", try again!")


screen.exitonclick()
