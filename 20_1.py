import turtle
import colorsys

turtle.speed(0)
turtle.bgcolor("black")
NUMBER_OF_PERTALS = 16
NUMBER_OF_PERTALS_VEINS = 18
hue = 0
for i in range (NUMBER_OF_PERTALS):
    for j in range(NUMBER_OF_PERTALS_VEINS):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        turtle.color(color)
        hue += 0.005
        turtle.right(90)
        radius = 150 - j * 6
        turtle.circle(radius, 90)
        turtle.left(90)
        turtle.circle(150 - j * 6, 90)
        turtle.right(180)
    turtle.circle(40,24)
