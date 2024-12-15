from turtle import Turtle

ALIGNMENT = "Left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center" ,font = FONT)
        
