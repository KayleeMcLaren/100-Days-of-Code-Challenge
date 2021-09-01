
from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [150, 100, 50, 0, -50, -100]
is_race_on = False
all_turtles = []

for turtle in range(0, 6):
  """Creates 6 turtles, setting them each a different colour from the colours list. Sets their starting positions at -230 on the x axis, 
  and thier y axis position is selected from the y_positions list. Each turtle is then appended to the all_turtles list"""
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(new_turtle)

if user_bet:
  """Allows the user to make their bet before the turtles start moving"""
    is_race_on = True

while is_race_on:
  """Each turtle moves forward at a randomly generated incremenet between 0 and 10. Also, checks to see if a turtle has won (which would be reaching the finish line on the other 
  side of the screen, at 230 on the x axis). Once a turtle has reached the finish line, the appropriate message is dispalyed in the console.""" 
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


my_screen.exitonclick()
