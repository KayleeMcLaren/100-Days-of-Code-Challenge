
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    """The Player class which creates the player's turtle character. It creates the movement for the player with the up fucntion. The go_to_start fucntion places the turtle
    at the starting position at the bottom of the screen. And the is_at_finish_line fucntion determines if the turtle has successfully made it across to the top of the screen"""
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
          
