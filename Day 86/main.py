import tkinter as tk
import time

# Sample text for the typing test
SAMPLE_TEXT = "The quick brown fox jumps over the lazy dog. Practice makes perfect and coding in Python is incredibly fun. Always try to improve your typing speed every single day."

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Typing Speed Test")
        self.root.geometry("750x520")
        self.root.config(padx=25, pady=25, bg="#F3F4F6")

        # State Variables
        self.time_left = 60
        self.timer_running = False
        self.start_time = None

        # --- UI Elements (Widgets) ---
        
        # 1. Title
        self.title_label = tk.Label(root, text="Typing Speed Test", font=("Arial", 22, "bold"), bg="#F3F4F6", fg="#1F2937")
        self.title_label.pack(pady=10)

        # 2. Timer Label
        self.timer_label = tk.Label(root, text="Time Left: 60s", font=("Arial", 14, "bold"), bg="#F3F4F6", fg="#DC2626")
        self.timer_label.pack(pady=5)

        # 3. Sample Text Display (Guide)
        self.sample_label = tk.Label(root, text=SAMPLE_TEXT, font=("Arial", 11), bg="#FFFFFF", fg="#4B5563", wraplength=680, justify="left", relief="solid", bd=1, padx=12, pady=12)
        self.sample_label.pack(pady=15)

        # 4. Text Input Area
        self.input_text = tk.Text(root, font=("Arial", 12), height=6, width=75, relief="solid", bd=1, wrap="word")
        self.input_text.pack(pady=10)
        
        # Event Binding: Triggers on key release to track typing progress
        self.input_text.bind("<KeyRelease>", self.check_typing)

        # 5. Results & Feedback Label
        self.result_label = tk.Label(root, text="Start typing the text above to begin the test!", font=("Arial", 11, "italic"), bg="#F3F4F6", fg="#059669")
        self.result_label.pack(pady=10)

        # 6. Reset Button
        self.reset_button = tk.Button(root, text="Reset Test", font=("Arial", 10, "bold"), bg="#3B82F6", fg="white", bd=0, padx=20, pady=8, command=self.reset_app)
        self.reset_button.pack(pady=10)

    def check_typing(self, event):
        """Starts the timer on the first keypress and checks if the text is complete."""
        if not self.timer_running and self.time_left == 60:
            self.timer_running = True
            self.start_time = time.time()
            self.update_countdown()

        user_content = self.input_text.get("1.0", "end-1c").strip()

        # If the user completed the exact text, stop the test immediately
        if user_content == SAMPLE_TEXT:
            self.end_test(finished_early=True)

    def update_countdown(self):
        """Handles the countdown clock per second."""
        if not self.timer_running:
            return  

        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_countdown)
        else:
            self.end_test(finished_early=False)

    def calculate_accuracy(self, user_text, sample_text):
        """Calculates typing accuracy percentage by comparing characters."""
        if not user_text:
            return 0
        
        correct_chars = 0
        min_length = min(len(user_text), len(sample_text))
        
        for i in range(min_length):
            if user_text[i] == sample_text[i]:
                correct_chars += 1
                
        accuracy = (correct_chars / len(user_text)) * 100
        return round(accuracy, 1)

    def end_test(self, finished_early):
        """Disables input and calculates final WPM and Accuracy metrics."""
        self.timer_running = False
        self.input_text.config(state="disabled")

        user_content = self.input_text.get("1.0", "end-1c").strip()
        words_typed = len(user_content.split())
        
        # Calculate Accuracy %
        accuracy = self.calculate_accuracy(user_content, SAMPLE_TEXT)

        if user_content:
            if finished_early:
                time_taken = time.time() - self.start_time
                minutes = time_taken / 60
                wpm = round(words_typed / minutes)
                message = f"🏆 Completed early in {round(time_taken, 1)}s!\n⏱️ Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%"
            else:
                wpm = words_typed
                message = f"⏱️ Time's up! Speed: {wpm} WPM | 🎯 Accuracy: {accuracy}%"
        else:
            message = "⚠️ No text was typed."

        self.result_label.config(text=message, font=("Arial", 13, "bold"), fg="#2563EB")

    def reset_app(self):
        """Resets the application back to its initial state."""
        self.time_left = 60
        self.timer_running = False
        self.start_time = None
        self.timer_label.config(text="Time Left: 60s")
        self.input_text.config(state="normal")
        self.input_text.delete("1.0", "end")
        self.result_label.config(text="Start typing the text above to begin the test!", font=("Arial", 11, "italic"), fg="#059669")

if __name__ == "__main__":
    window = tk.Tk()
    app = TypingSpeedApp(window)
    window.mainloop()
