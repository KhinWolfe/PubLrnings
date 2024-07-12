from turtle import Turtle, Screen, colormode
import random

color_list = [(181, 171, 162),(185, 177, 180), (211, 194, 157), (159, 78, 48),
              (153, 179, 158), (40, 109, 133), (156, 176, 185), (48, 126, 90),
              (212, 182, 177), (175, 150, 44), (205, 183, 187), (137, 70, 80),
              (153, 23, 31), (142, 29, 21), (204, 91, 67), (12, 99, 77),
              (70, 45, 35), (94, 148, 110), (181, 198, 188), (73, 148, 167),
              (22, 64, 86), (63, 44, 50), (193, 77, 85), (11, 89, 104),
              (186, 191, 199), (168, 202, 208)]

#todo create painting with 10 x 10 rows of spots
#todo dots 20 in size and spaced 50
colormode(255)
timmy = Turtle()
timmy.color(random.choice(color_list))
timmy.speed("fastest")
timmy.up()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.down()
print(timmy.pos())
for row in range(10):
    timmy.up()
    timmy.setpos(-200 ,-200 + (50 * (row + 1) ))
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.up()
        timmy.forward(50)
        timmy.down()
timmy.hideturtle()



screen = Screen()
screen.exitonclick()