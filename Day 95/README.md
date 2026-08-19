# 👾 Space Invaders

A classic Space Invaders arcade game clone, built with Python Turtle.

Built as part of the **100 Days of Code** Udemy course assignment (Day 95).

---

## ✨ Features

- A player ship that moves left/right and fires lasers with a cooldown (no spamming)
- A fleet of 28 aliens (4 rows × 7 columns), each row a different color, that moves as a group and steps down whenever it hits a screen edge
- 3 destructible barrier bunkers, each made of individual blocks that can absorb hits
- Score tracking, and both Game Over and You Win end states

---

## 🎮 Controls

| Key | Action |
|---|---|
| `←` | Move left |
| `→` | Move right |
| `Space` | Fire laser |

---

## 🛠 Built With

- Python 3
- `turtle` (built into Python — no installation needed)

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📁 Project Structure

```
space_invaders/
├── main.py          ← game loop, collisions, keyboard controls
├── player.py         ← the player's ship
├── laser.py           ← laser shots
├── alien.py            ← individual aliens + fleet creation
├── barrier.py            ← destructible barrier bunkers
└── scoreboard.py           ← score, lives, game-over/win messages
```

Each game "actor" lives in its own file as a class inheriting from `turtle.Turtle`, and `main.py` ties them all together in a single game loop.

---

## 🧠 How It Works

- **Fleet movement:** all aliens move together each frame. When any alien reaches a screen edge, the whole fleet reverses direction and steps down one row — the classic Space Invaders zig-zag pattern.
- **Barriers:** built from a simple grid pattern (a list of lists of 1s and 0s) that maps directly onto small block positions, creating the classic arch shape with gaps.
- **Collision detection:** uses Turtle's built-in `.distance()` method to check how close two objects are, rather than manual pixel/geometry math.
- **Screen updates:** `screen.tracer(0)` disables automatic redrawing, and `screen.update()` is called once per game loop iteration — this batches all movement into a single redraw per frame, giving smooth animation instead of flickering.

---

## 💭 Reflection

*(Fill this in after building — this section is part of the assignment)*

- **How did I approach the project?**
- **What was hard? What was easy?**
- **What would I do differently next time?**
- **Biggest learning from today?**

---

## 📌 Possible Improvements

- Increase alien movement speed as fewer aliens remain (matches the original arcade game's difficulty curve)
- Add alien lasers firing back at the player (the `Laser` class already supports a `direction` parameter for this)
- Add a lives system instead of instant game-over (the `Scoreboard.lose_life()` method is already there, just unused)
- Add sound effects for shooting and explosions

---

## 📄 License

Free to use for learning purposes.
