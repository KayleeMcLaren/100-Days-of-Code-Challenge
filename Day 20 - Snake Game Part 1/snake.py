
from turtle import Turtle

X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_squares_list = []
        self.create_snake()
        self.snake_head = self.snake_squares_list[0]
        

    def create_snake(self):
      """Creates 3 segments for the Snake which are square shaped and white in colour. It also sets the starting postion so that each segment is right next to each other,
      without any spaces in between them. This is so that the Snake looks like it's one long segment. Each segment is appended to the self.snake_squares_list"""
        for snake_square_index in range(0, 3):
            new_snake_square = Turtle()
            new_snake_square.penup()
            new_snake_square.color("white")
            new_snake_square.shape("square")
            new_snake_square.goto(x=X_POSITIONS[snake_square_index], y=0)
            self.snake_squares_list.append(new_snake_square)
            

    def move(self):
      """Creates the movement for the Snake. The for loop iterates through snake_squares_list backwards (-1), starting with the last index (finding the length of the 
      snake_suares_list -1) and ending at the first index (index 0). The movement is such that the last segment goes to the x and y postion of the second to last segment."""
        for snake_segment in range(len(self.snake_squares_list) - 1, 0, -1):
            new_x = self.snake_squares_list[snake_segment - 1].xcor() # gets the x coordinate of the second to last segment
            new_y = self.snake_squares_list[snake_segment - 1].ycor() # gets the y coordinate of the second to last segment
            self.snake_squares_list[snake_segment].goto(new_x, new_y) # uses .goto to get the last segment to go to the positon of the second to last segment

        self.snake_head.forward(MOVE_DISTANCE) # Snake moves forwards
        
        
    """Functions which change the direction of the Snake by setting the heading. Also ensures that the Snake cannot move backwards (or opposite the current direction). 
    So if the Snake is moving towards the Right, it cannot reverse itself direction and move towards the Left , only Up or Down"""
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

