import time
from turtle import Screen, Turtle

# 1. Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)  # Turns off automatic screen updates for smoother rendering

# 2. Create the Paddle
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)  # Stretches the paddle to 100px width
paddle.penup()
paddle.goto(0, -250)

# 3. Create the Ball
ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -100)  # Starts slightly lower than the center
ball.x_move = 5     # Horizontal speed/direction
ball.y_move = 5     # Vertical speed/direction (initially moving UP)

# 4. Create the Bricks Grid
all_bricks = []
colors = ["red", "orange", "yellow", "green"]

# Nested loop to generate a grid of 4 rows and 15 columns
for row in range(4):
    for col in range(-7, 8):
        brick = Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=2.5)  # Sizes the brick
        brick.penup()
        
        # Calculate X and Y coordinates to arrange bricks neatly with small gaps
        x_pos = col * 53
        y_pos = 220 - (row * 30)
        
        brick.goto(x_pos, y_pos)
        all_bricks.append(brick)

# Update the screen once to draw all elements before the game starts
screen.update()

# 5. Paddle Movement Functions
def go_right():
    new_x = paddle.xcor() + 40
    if new_x < 350:  # Boundary check for the right edge
        paddle.goto(new_x, paddle.ycor())

def go_left():
    new_x = paddle.xcor() - 40
    if new_x > -350:  # Boundary check for the left edge
        paddle.goto(new_x, paddle.ycor())

# Keyboard Listening
screen.listen()
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

# 6. Main Game Loop
game_is_on = True
while game_is_on:
    time.sleep(0.02)  # Controls game speed / frame rate
    screen.update()   # Manually refreshes the screen animation
    
    # Move the ball
    new_x = ball.xcor() + ball.x_move
    new_y = ball.ycor() + ball.y_move
    ball.goto(new_x, new_y)

    # Wall Collision (Left / Right edges)
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.x_move *= -1

    # Ceiling Collision (Top edge)
    if ball.ycor() > 280:
        ball.y_move *= -1

    # Paddle Collision (Ball hits the paddle)
    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.y_move *= -1

    # Brick Collision (Ball hits a brick)
    for brick in all_bricks:
        if ball.distance(brick) < 30:
            brick.hideturtle()        # Visually hides the brick
            all_bricks.remove(brick)  # Removes the brick from the active list
            ball.y_move *= -1         # Bounces the ball back
            break                     # Breaks out of the loop for this frame

    # Win Condition (All bricks destroyed)
    if len(all_bricks) == 0:
        game_is_on = False
        print("You Win! Congratulations!")

    # Game Over Condition (Ball falls past the paddle)
    if ball.ycor() < -280:
        game_is_on = False
        print("Game Over!")

screen.exitonclick()
