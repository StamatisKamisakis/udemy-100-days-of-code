from turtle import Turtle

MOVE_DISTANCE = 25


class Laser(Turtle):
    """A single laser shot. Moves straight up (or down, for alien lasers)."""

    def __init__(self, position, color="yellow", direction=1):
        """
        direction=1 means the laser moves up (fired by the player).
        direction=-1 means it moves down (could be used for alien fire later).
        """
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=0.2, stretch_len=0.6)
        self.setheading(90)
        self.penup()
        self.goto(position)
        self.direction = direction

    def move(self):
        self.goto(self.xcor(), self.ycor() + (MOVE_DISTANCE * self.direction))

    def is_off_screen(self):
        return self.ycor() > 380 or self.ycor() < -380
