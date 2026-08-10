"""
Coordinate Finder — run this FIRST.
------------------------------------
This tiny helper continuously prints your mouse's screen coordinates and
the color of the pixel underneath it, once per second.

How to use it:
1. Open https://elgoog.im/t-rex/ in your browser, and position the browser
   window somewhere on screen (don't move it after this step).
2. Run this script.
3. Hover your mouse right above the ground line, just in front of the
   dinosaur — this is where cactus obstacles will appear as it runs.
4. Note down the (x, y) coordinates printed, and the "background" color
   (should be white-ish, e.g. close to (255, 255, 255)) — you'll need
   both for dino_bot.py.
5. Press Ctrl+C to stop this script once you have the numbers.
"""

import time
import pyautogui

print("Move your mouse over the spot just in front of the dinosaur.")
print("Press Ctrl+C to stop once you have your coordinates.\n")

try:
    while True:
        x, y = pyautogui.position()
        pixel_color = pyautogui.pixel(x, y)
        print(f"Mouse position: ({x}, {y})   Pixel color: {pixel_color}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped. Use these coordinates in dino_bot.py.")