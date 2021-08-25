from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/48516/OneDrive - Politechnika Warszawska/MyPython/kurs/100_Days_of_code/Day_20/.vscode/data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High score: {self.highscore}", align =ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    '''
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        '''

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("/Users/48516/OneDrive - Politechnika Warszawska/MyPython/kurs/100_Days_of_code/Day_20/.vscode/data.txt",'w') as data:
                data.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard() 

        