
import random
import turtle

import colorgram
from turtle import Turtle, Screen

"""Uses the colorgram package to extract the colours from a real Hirst painting to use in the program. It's commented out as it doesn't need to be run every time"""
#colours = colorgram.extract('hirst.jpg', 30) # extracts 30 colours from a jpeg image of a hirst painting

#colour_list = []
#for colour in colours:
"""From the extracted colours in the colours list, each individual colour has the values of it's red, green, and blue composition saved as a tuple called new_colour and 
added to a list of tuples called colour_list"""
    #g = colour.rgb.g
    #b = colour.rgb.b
    #new_colour = (r, g, b)
    #colour_list.append(new_colour)

#print(colour_list)

turtle.colormode(255)

"""hirst_colours is made up of the values in the colour_list, copied from the terminal after line 20 was run"""
hirst_colours = [(249, 243, 247), (1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]

shelly = Turtle()
shelly.hideturtle() # makes the turtle invisible

"""Sets the turtle's starting position from the center of the screen, to closer to the lower left hand corner"""
shelly.penup()
shelly.setheading(225)
shelly.forward(250)
shelly.setheading(0)

number_of_dots = 101

for dot_count in range(1, number_of_dots):
  """Draws the rows of dots"""
    shelly.penup()
    shelly.dot(20, random.choice(hirst_colours)) 
    shelly.forward(50)

    """Uses an if statement to check the number of dots in each row (there should be 10). So for example it will draw dots in the first row (in the range 1 to 101), until it 
    reaches the number 10 as the will make the if statement True and trigger the code in that if statement. This will move the turtle back to the left hand side of the painting 
    and facing the right so that it's in the correct position to draw the next row of dots. It will continue drawing until it reaches the number 20 and then will move to the left 
    again, and repeat this until out of range"""
    if dot_count % 10 == 0:
        shelly.setheading(90)
        shelly.forward(50)
        shelly.setheading(180)
        shelly.forward(500)
        shelly.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
