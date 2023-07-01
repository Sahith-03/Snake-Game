from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score:{self.score} High Score:{self.highscore}",align ="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=("Arial",24, "normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("highscore.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))