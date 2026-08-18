from turtle import Turtle

FONT = ("Courier", 16, "normal")
GAME_OVER_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    """Displays the current score, lives, and the game-over message."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-380, 350)
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(
            f"Score: {self.score}    Lives: {self.lives}",
            align="left",
            font=FONT,
        )

    def increase_score(self, points=10):
        self.score += points
        self.update_display()

    def lose_life(self):
        self.lives -= 1
        self.update_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
