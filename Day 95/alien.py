from turtle import Turtle

ALIEN_COLORS = ["red", "orange", "purple", "white", "yellow"]

ROWS = 4
COLUMNS = 7
ROW_SPACING = 50
COLUMN_SPACING = 60
FLEET_START_Y = 250


class Alien(Turtle):
    """A single alien invader."""

    def __init__(self, position, color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.penup()
        self.goto(position)

    def move_down(self, distance):
        self.goto(self.xcor(), self.ycor() - distance)


def create_fleet():
    """
    Builds a grid of aliens (ROWS x COLUMNS), centered horizontally.
    Each row gets a different color, just like the classic arcade game.
    Returns a list of Alien objects.
    """
    fleet = []
    total_width = (COLUMNS - 1) * COLUMN_SPACING
    start_x = -total_width / 2

    for row in range(ROWS):
        color = ALIEN_COLORS[row % len(ALIEN_COLORS)]
        y = FLEET_START_Y - (row * ROW_SPACING)

        for col in range(COLUMNS):
            x = start_x + (col * COLUMN_SPACING)
            fleet.append(Alien((x, y), color))

    return fleet
