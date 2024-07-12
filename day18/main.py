from turtle import Turtle, Screen, colormode
import random

colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("CadetBlue4")
edges = 4
angle = 90
penColors = ["blue", "red", "green", "purple", "yellow", "black", "orange"]

directions = [0, 90, 180, 270]
timmy.pensize(1)
timmy.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColor = (r, g, b)
    return randomColor


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        # timmy.forward(30)
        # timmy.right(random.choice(directions))
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)










screen = Screen()
screen.exitonclick()