from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
winning_color = ""
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color_list = ["red", "blue", "green", "yellow", "purple", "orange"]
all_turtles = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
def color_turtle():
    color1 = 0
    for turtle in all_turtles:
        turtle.color(color_list[color1])
        color1 += 1

def starting_pos():
    row = 0
    for turtle in all_turtles:
        turtle.up()
        turtle.goto(x=-230, y=(-100 + row))
        row += 40
def watch_winner():
    global winning_color
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            return False
    return True
def race_turtles():
    for turtle in all_turtles:
        turtle.forward((random.randint(1, 3) * 10))

# timmy.up()
# timmy.goto(x=-230,y=-100)
color_turtle()
starting_pos()
if user_bet:
    is_race_on = True

while is_race_on:
    race_turtles()
    is_race_on = watch_winner()
if winning_color == user_bet.lower():
    print("You've Won!")
else:
    print("You've lost!")
print(f"The {winning_color} turtle is the winner!")
screen.exitonclick()