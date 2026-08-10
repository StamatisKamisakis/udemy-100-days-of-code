"""
Dino Game Bot
--------------
Watches a single pixel just in front of the dinosaur. When that pixel's
color changes (an obstacle has appeared there), it presses the space bar
to make the dinosaur jump.

SETUP REQUIRED before running:
1. Run find_coordinates.py first to get YOUR screen's coordinates and
   background color (these depend on your screen resolution, browser
   zoom level, and window position — they're different for everyone).
2. Fill in OBSTACLE_X, OBSTACLE_Y, and BACKGROUND_COLOR below with the
   values you found.
3. Open https://elgoog.im/t-rex/ and keep the window in the exact same
   position you used for calibration.
4. Run this script, then quickly click on the game window to focus it.

Requirements (install once):
    pip install pyautogui pillow
"""

import time
import pyautogui

# ---------- FILL THESE IN AFTER RUNNING find_coordinates.py ----------
OBSTACLE_X = 579
OBSTACLE_Y = 559
BACKGROUND_COLOR = (255, 255, 255)

# OBSTACLE_X = 300   # <-- replace with your x coordinate
# OBSTACLE_Y = 300   # <-- replace with your y coordinate
# BACKGROUND_COLOR = (255, 255, 255)  # <-- replace with your background pixel color
# -----------------------------------------------------------------------

# How different a color can be from BACKGROUND_COLOR before we treat it
# as "an obstacle is here". A small tolerance avoids false triggers from
# minor rendering differences (anti-aliasing, slight color variation).
COLOR_TOLERANCE = 30

CHECK_INTERVAL = 0.01  # seconds between each pixel check — keep this small
                        # so we don't miss fast-moving obstacles


def colors_are_different(color_a, color_b, tolerance):
    """
    Compares two RGB colors and returns True if they differ by more than
    `tolerance` in any channel (Red, Green, or Blue).
    """
    r1, g1, b1 = color_a[:3]
    r2, g2, b2 = color_b[:3]
    return (
        abs(r1 - r2) > tolerance
        or abs(g1 - g2) > tolerance
        or abs(b1 - b2) > tolerance
    )
 

def start_game():
    """Clicks the game area to focus it, then presses space to start."""
    pyautogui.click(OBSTACLE_X, OBSTACLE_Y)
    time.sleep(0.5)
    pyautogui.press("space")
    print("Game started! Watching for obstacles...")


def watch_and_jump():
    """Main loop: checks the obstacle pixel and jumps when it changes color."""
    while True:
        current_color = pyautogui.pixel(OBSTACLE_X, OBSTACLE_Y)

        if colors_are_different(current_color, BACKGROUND_COLOR, COLOR_TOLERANCE):
            pyautogui.press("space")
            # Small pause after jumping so we don't spam multiple jumps
            # for the same obstacle while it's still passing the checkpoint.
            time.sleep(0.3)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    print("Starting in 3 seconds — switch to your browser window now!")
    time.sleep(3)

    start_game()

    try:
        watch_and_jump()
    except KeyboardInterrupt:
        print("\nBot stopped.")
