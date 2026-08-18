"""
Space Invaders — Python Turtle
--------------------------------
Controls:
    Left / Right arrow  -> move the ship
    Spacebar             -> fire a laser

Goal: destroy all the aliens before they reach your ship.
The barriers (green blocks) can absorb a limited number of hits and
give you cover, but each block is destroyed after a single hit.
"""

import time
from turtle import Screen

from player import Player
from laser import Laser
from alien import create_fleet
from barrier import create_barriers
from scoreboard import Scoreboard

# ---------- SCREEN SETUP ----------
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)  # turn off automatic screen updates — we control them manually for smooth animation

# ---------- GAME OBJECTS ----------
player = Player()
scoreboard = Scoreboard()
aliens = create_fleet()
barriers = create_barriers()
lasers = []

# ---------- CONSTANTS ----------
ALIEN_MOVE_DISTANCE = 4
ALIEN_STEP_DOWN = 30
LASER_COOLDOWN = 0.4  # seconds between shots, so holding space doesn't spam lasers
COLLISION_DISTANCE = 20
GAME_OVER_Y = -260  # if an alien reaches this height, it's game over

fleet_direction = 1  # 1 = moving right, -1 = moving left
last_shot_time = 0


def fire_laser():
    """Creates a new laser at the player's current position, respecting a cooldown."""
    global last_shot_time
    now = time.time()
    if now - last_shot_time >= LASER_COOLDOWN:
        new_laser = Laser(player.position(), color="yellow", direction=1)
        lasers.append(new_laser)
        last_shot_time = now


# ---------- KEYBOARD CONTROLS ----------
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(fire_laser, "space")

# ---------- MAIN GAME LOOP ----------
game_is_on = True

while game_is_on:
    time.sleep(0.02)
    screen.update()

    # --- Move all lasers, remove any that left the screen ---
    for laser in lasers[:]:
        laser.move()
        if laser.is_off_screen():
            laser.hideturtle()
            lasers.remove(laser)

    # --- Move the alien fleet as a group ---
    for alien in aliens:
        alien.goto(alien.xcor() + (ALIEN_MOVE_DISTANCE * fleet_direction), alien.ycor())

    # Check if any alien hit the left/right screen edge — if so, reverse
    # direction and step the whole fleet down (classic Space Invaders behavior).
    edge_hit = any(alien.xcor() > 380 or alien.xcor() < -380 for alien in aliens)
    if edge_hit:
        fleet_direction *= -1
        for alien in aliens:
            alien.move_down(ALIEN_STEP_DOWN)

    # --- Check laser-vs-alien collisions ---
    for laser in lasers[:]:
        for alien in aliens[:]:
            if laser.distance(alien) < COLLISION_DISTANCE:
                alien.hideturtle()
                aliens.remove(alien)
                laser.hideturtle()
                if laser in lasers:
                    lasers.remove(laser)
                scoreboard.increase_score(10)
                break  # this laser is used up, stop checking it against other aliens

    # --- Check laser-vs-barrier collisions ---
    for laser in lasers[:]:
        for block in barriers[:]:
            if laser.distance(block) < COLLISION_DISTANCE:
                block.hideturtle()
                barriers.remove(block)
                laser.hideturtle()
                if laser in lasers:
                    lasers.remove(laser)
                break

    # --- Check if any alien reached the player's row (game over) ---
    if any(alien.ycor() < GAME_OVER_Y for alien in aliens):
        game_is_on = False
        scoreboard.game_over()

    # --- Check win condition: no aliens left ---
    if not aliens:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))

screen.exitonclick()
