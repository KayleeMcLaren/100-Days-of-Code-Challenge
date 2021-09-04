
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Rockwell", 24, "normal")

"""The Scoreboard class is used to display a scoreboard on the screen using the update_screen function. 
It increases the score with the increase_score fucntion and displays Game Over with the game_over fucntion."""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        
