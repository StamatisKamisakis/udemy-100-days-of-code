# 🔥 Dangerous Writing App

A desktop app built with **Python** and **Tkinter**, inspired by [The Most Dangerous Writing App](https://www.squibler.io/dangerous-writing-prompt-app).

The idea is simple: it forces you to keep writing. If you stop typing for more than **5 seconds**, everything you've written gets deleted.

This was built as part of the **100 Days of Code** Udemy course assignment.

---

## ✨ Features

- Live countdown timer displayed on screen
- Typing resets the timer back to 5 seconds
- Stopping for 5+ seconds wipes the entire text box
- Simple dark-themed UI

---

## 🛠 Built With

- Python 3
- Tkinter (built into Python, no extra install needed)

---

## ▶️ How to Run

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```
2. Clone this repo (or just download the `.py` file)
3. Run the app:
   ```bash
   python dangerous_writing_app.py
   ```

No external dependencies required.

---

## 🧠 How It Works

- `window.after(1000, countdown)` schedules the `countdown()` function to run every 1 second, without freezing the app.
- Every keystroke triggers `reset_timer()`, which resets the counter back to 5 and cancels the previously scheduled countdown (`window.after_cancel`), preventing multiple timers from stacking up.
- When the counter hits 0, `text_box.delete("1.0", END)` clears the text box — `"1.0"` means "line 1, character 0" (the very start), and `END` means "the very end of the text."

---

## 💭 Reflection

*(Fill this in after building — this section is part of the assignment)*

- **How did I approach the project?**
- **What was hard? What was easy?**
- **What would I do differently next time?**
- **Biggest learning from today?**

---

## 📌 Possible Improvements

- Add a warning sound before the timer hits 0
- Auto-save text to a file before it gets deleted
- Add a "word count" goal instead of (or alongside) the timer
- Add difficulty levels (3s / 5s / 10s time limits)

---

## 📄 License

Free to use for learning purposes.
