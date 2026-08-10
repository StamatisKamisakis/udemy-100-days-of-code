# 🦖 Google Dinosaur Game Bot

A Python bot that automatically plays the Chrome "T-Rex Runner" game (the one that shows up when you're offline) by watching a single pixel on screen and pressing the space bar when an obstacle is detected.

Built as part of the **100 Days of Code** Udemy course assignment (Day 94).

---

## ✨ How it works

Instead of reading the game's internal state through code, this bot plays the way a very literal robot would: it watches **one fixed point on screen**, just ahead of the dinosaur. When that point's color changes from the background (white) to something darker (a cactus), it presses space to jump.

- `find_coordinates.py` — a small helper that prints your mouse's live screen coordinates and the pixel color underneath it, used to calibrate the bot's "watch point" for your specific screen/browser setup
- `dino_bot.py` — the actual bot: starts the game and continuously watches the calibrated point, jumping whenever it detects a color change

---

## 🛠 Built With

- Python 3
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — reads screen pixel colors and controls mouse/keyboard
- [Pillow](https://pypi.org/project/Pillow/) — used internally by PyAutoGUI for screenshots

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install pyautogui pillow
   ```
2. Open [https://elgoog.im/t-rex/](https://elgoog.im/t-rex/) in your browser and position the window — don't move it after this step.
3. Run the coordinate finder to calibrate for your screen:
   ```bash
   python find_coordinates.py
   ```
   Hover your mouse over a point on the ground, ahead of the dinosaur, and note the (x, y) coordinates and background color it prints.
4. Open `dino_bot.py` and fill in your values:
   ```python
   OBSTACLE_X = <your x>
   OBSTACLE_Y = <your y>
   BACKGROUND_COLOR = <your background color>
   ```
5. Run the bot:
   ```bash
   python dino_bot.py
   ```
   Switch to your browser window within the 3-second countdown.

**Note:** If you use a browser extension like Dark Reader, disable it for the game page first — it changes the page's actual on-screen colors, which throws off the pixel detection entirely.

---

## 🧠 Key Design Notes

- The bot re-checks the pixel color every 10ms (`CHECK_INTERVAL`), fast enough to catch obstacles at typical game speed.
- A short cooldown after each jump prevents the same obstacle from triggering multiple jumps while it passes through the watch point.
- **Trade-off discovered while testing:** the watch point's distance from the dinosaur matters a lot. Too close, and the bot doesn't have time to react. Too far, and the jump (which has a fixed duration) can finish *before* the obstacle arrives, causing the dinosaur to land right back down on it. Finding a good distance took some manual trial and error.
- The game's speed increases over time, meaning a fixed watch-point distance eventually becomes too short for the bot to react in time — the bot works reliably early in a run and becomes less reliable as the game speeds up.

---

## 💭 Reflection

*(Fill this in after building — this section is part of the assignment)*

- **How did I approach the project?**
- **What was hard? What was easy?**
- **What would I do differently next time?**
- **Biggest learning from today?**

---

## 📌 Possible Improvements

- Dynamically increase the watch-point distance over time to compensate for the game speeding up
- Watch multiple points at different distances instead of just one, for more reliable early detection
- Detect "duck" obstacles (birds) separately, since jumping isn't always the right move for those
- Add automatic game-over detection to restart the run without manual intervention

---

## 📄 License

Free to use for learning purposes.
