# Day 87: Breakout Game 🎮

A classic arcade Breakout game built from scratch using **Python** and the **Turtle Graphics** library. This project was developed as a Capstone Project for Day 87 of the *"100 Days of Code: The Complete Python Pro Bootcamp"* by Angela Yu.

The objective of the game is to control a paddle at the bottom of the screen to bounce a ball and destroy all the colored bricks at the top without letting the ball fall past the paddle.

---

## 🚀 Features

* **Grid Generation:** Automatically builds a $4 \times 15$ grid of bricks with distinct color rows (Red, Orange, Yellow, Green) and custom padding.
* **Physics & Bouncing:** Features responsive collision detection for walls, the ceiling, and the moving paddle.
* **Win/Loss States:** The game detects when all bricks are smashed (Victory) or when the ball falls off the bottom edge (Game Over).
* **Smooth Rendering:** Utilizes `screen.tracer(0)` and manual frame updates to completely eliminate animation lag or flickering.

---

## 🛠️ Tech Stack & Concepts Used

* **Language:** Python 3
* **Graphics:** Built-in `turtle` module (Object-Oriented Programming approach).
* **Time Management:** Python's `time` module for frame-rate pacing.
* **Core Concepts:** Nested loops for coordinate geometry, multidimensional grid spacing, list manipulation, and collision boundaries.

---

## 🎮 How to Play

### 📋 Prerequisites
Make sure you have Python installed on your system. The `turtle` and `time` modules come pre-installed with Python, so no external packages are required!

### 🔧 Installation & Running
1. Clone this repository or download the source code:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/breakout-game.git](https://github.com/YOUR_USERNAME/breakout-game.git)