from turtle import Turtle

BARRIER_COLOR = "green"
BLOCK_SIZE = 0.8  # shapesize multiplier for each small block
BLOCK_SPACING = 16

# How many barrier "bunkers" to place, and where (x positions)
BARRIER_X_POSITIONS = [-200, 0, 200]
BARRIER_Y = -180

# A simple grid pattern for one bunker: 1 = block present, 0 = empty.
# This shapes it roughly like the classic arcade bunkers (arch shape).
BUNKER_PATTERN = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
]


class BarrierBlock(Turtle):
    """A single small block of a defensive barrier. Destroyed on one hit."""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(BARRIER_COLOR)
        self.shapesize(stretch_wid=BLOCK_SIZE, stretch_len=BLOCK_SIZE)
        self.penup()
        self.goto(position)


def create_barriers():
    """
    Builds several barrier bunkers, each made of many small blocks arranged
    in BUNKER_PATTERN. Returns a flat list of all BarrierBlock objects.
    """
    blocks = []

    for bunker_x in BARRIER_X_POSITIONS:
        pattern_width = len(BUNKER_PATTERN[0]) * BLOCK_SPACING
        start_x = bunker_x - pattern_width / 2

        for row_index, row in enumerate(BUNKER_PATTERN):
            y = BARRIER_Y - (row_index * BLOCK_SPACING)
            for col_index, cell in enumerate(row):
                if cell == 1:
                    x = start_x + (col_index * BLOCK_SPACING)
                    blocks.append(BarrierBlock((x, y)))

    return blocks
