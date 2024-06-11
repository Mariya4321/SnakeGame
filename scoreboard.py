from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("HighScore.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}, HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def score_inc(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("HighScore.txt", mode="w") as file:
            file.write(f"{self.highscore}")
        self.score = 0
        self.update()
