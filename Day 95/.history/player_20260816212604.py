from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
SCREEN_LIMIT = 280


class Player(Turtle):
    """The player's spaceship — moves left/right at the bottom of the screen."""

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("cyan")
        self.shapesize(stretch_wid=1.2, stretch_len=1.5)
        self.setheading(90)  # point the triangle upward
        self.penup()
        self.goto(STARTING_POSITION)

    def move_left(self):
        if self.xcor() > -SCREEN_LIMIT:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        if self.xcor() < SCREEN_LIMIT:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

