from tkinter import *

# ---------- SETTINGS ----------
FONT = ("Arial", 20, "normal")
TIME_LIMIT = 5  # seconds of inactivity allowed before the text gets wiped

# ---------- WINDOW ----------
window = Tk()
window.title("The Most Dangerous Writing App")
window.config(padx=30, pady=30, bg="#2b2b2b")

# ---------- TIMER DISPLAY ----------
timer_label = Label(window, text=f"⏱ {TIME_LIMIT}", font=("Arial", 16, "bold"),
                     bg="#2b2b2b", fg="#ff5555")
timer_label.pack(pady=(0, 10))

# ---------- TEXT BOX ----------
text_box = Text(window, width=60, height=20, font=FONT, wrap="word",
                 bg="#1e1e1e", fg="white", insertbackground="white",
                 relief="flat", padx=10, pady=10)
text_box.pack()
text_box.focus()  # so the user can start typing immediately

# ---------- TIMER LOGIC ----------
seconds_left = TIME_LIMIT
timer_id = None  # holds the "ticket" for the currently scheduled after() call


def countdown():
    global seconds_left, timer_id

    timer_label.config(text=f"⏱ {seconds_left}")

    if seconds_left <= 0:
        # Time's up -> wipe everything the user has written
        text_box.delete("1.0", END)
        seconds_left = TIME_LIMIT
    else:
        seconds_left -= 1

    # Reschedule itself to run again in 1000ms (1 second)
    timer_id = window.after(1000, countdown)


def reset_timer(event=None):
    """Called every time the user presses a key."""
    global seconds_left, timer_id

    seconds_left = TIME_LIMIT

    if timer_id is not None:
        window.after_cancel(timer_id)  # cancel the previously scheduled countdown

    timer_id = window.after(1000, countdown)  # start a fresh countdown


# Listen for every keystroke inside the text_box
text_box.bind("<Key>", reset_timer)

# Start the first countdown as soon as the app opens
timer_id = window.after(1000, countdown)

window.mainloop()
