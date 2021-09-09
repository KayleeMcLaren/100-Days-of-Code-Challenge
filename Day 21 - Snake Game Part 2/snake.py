
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""The Snake class creates the snake object using the create_snake function. It increases the length of the snake after it collides with 
the food object using the add_segment function and the extend function. If the user's loses a round of the game, the reset function removes 
the segments which the user aquired during the round and moves them to co ordinates to make ure they are not visible to the user it calls the 
create_snake fucntion to set the snake to the starting position for the next round of the game. It also creates the snake's movement using 
the movement function and the directional functions up, down, left, and right."""
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_square = Turtle()
        new_snake_square.penup()
        new_snake_square.color("white")
        new_snake_square.shape("square")
        new_snake_square.goto(position)
        self.segments.append(new_snake_square)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for snake_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_segment - 1].xcor()
            new_y = self.segments[snake_segment - 1].ycor()
            self.segments[snake_segment].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
            
