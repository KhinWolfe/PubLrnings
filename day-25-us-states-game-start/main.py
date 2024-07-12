import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
count = 0
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
state_print = turtle.Turtle()
state_print.up()
state_print.hideturtle()
guessed_states = []

data = pandas.read_csv("50_states.csv")

list_states = data.state.to_list()

while len(guessed_states) < len(list_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing = [state for state in list_states if state not in guessed_states]
        print(missing)
        break
    for state in list_states:
        if answer_state == state:
            if state not in guessed_states:
                guessed_states.append(answer_state)
                t = turtle.Turtle()
                t.hideturtle()
                t.up()
                row = data[data.state == answer_state]
                t.goto(int(row.x), int(row.y))
                t.write(f"{answer_state}")

