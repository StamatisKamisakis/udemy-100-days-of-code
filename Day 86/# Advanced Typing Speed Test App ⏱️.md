# Advanced Typing Speed Test App ⏱️🎯

A clean, modern, and lightweight Desktop Application built with Python and Tkinter to measure typing speed (WPM) and character accuracy. This project is ideal for portfolio building and Python GUI educational courses.

## Features ✨

* **Real-time Event Tracking:** Starts the countdown automatically on the very first keystroke.
* **Early Completion Detection:** Detects if the user finishes the text before 60 seconds and stops the timer instantly.
* **Dynamic WPM Calculation:** Computes accurate Words Per Minute (WPM) adjusted to the exact seconds taken.
* **Character-Level Accuracy:** Compares input text against the sample text string-by-string to yield a precise percentage (`% Accuracy`).
* **Responsive UI:** Clean typography and layouts utilizing modern design color palettes (`Hex #F3F4F6`, `#2563EB`).

## Requirements 🛠️

* Python 3.x
* Tkinter (included by default with standard Python installations)

## Installation & Setup 🚀

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```

2. Navigate into the project folder:
   ```bash
   cd "Day 86"
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## How It Works 💻

* **`__init__`**: Initializes the main application window, sizes, and layout widgets.
* **`check_typing`**: Binds to `<KeyRelease>` events to automatically evaluate string equality and manage early-finish states.
* **`calculate_accuracy`**: Calculates character matches dividing correct indices by total length typed.
* **`update_countdown`**: Uses Tkinter’s `.after()` loop method to cleanly decrement remaining seconds without freeze issues.

## Project Structure 📁

```text
├── main.py          # Main application file containing Python source code
└── README.md        # Documentation and guide file
```

## License 📄

This project is open-source and available under the [MIT License](LICENSE).
