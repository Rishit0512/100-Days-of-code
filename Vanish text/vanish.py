import tkinter as tk
from tkinter import StringVar
import time

class AutoClearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto-Delete Text with Timer")

        # Initialize variables
        self.typing_timer = None
        self.typing_delay = 5000  # 5 seconds in milliseconds
        self.last_keypress_time = time.time()
        
        # Set up the UI
        self.setup_ui()

        # Start the countdown update loop
        self.update_timer()

    def setup_ui(self):
        # Create and place a text widget
        self.text_input = tk.Text(self.root, wrap='word', width=60, height=15, bg='#1e1e1e', fg='#e0e0e0', insertbackground='white')
        self.text_input.pack(pady=10)

        # Create and place a label for the countdown timer
        self.timer_var = StringVar()
        self.timer_var.set("Time left: 5.00 seconds")
        self.timer_label = tk.Label(self.root, textvariable=self.timer_var, fg='#b0b0b0', bg='#121212', font=('Arial', 18))
        self.timer_label.pack(pady=10)

        # Bind the key release event to the handler
        self.text_input.bind('<KeyRelease>', self.reset_timer)

    def reset_timer(self, event):
        # Reset the typing timer whenever a key is released
        self.last_keypress_time = time.time()
        self.start_timer()

    def start_timer(self):
        # Cancel any existing timer
        if self.typing_timer:
            self.root.after_cancel(self.typing_timer)
        
        # Set up a new timer to clear text after the delay
        self.typing_timer = self.root.after(self.typing_delay, self.clear_text)

    def clear_text(self):
        # Clear the text area and reset the timer display
        self.text_input.delete('1.0', tk.END)
        self.timer_var.set("Time left: 5.00 seconds")

        # Restart the countdown
        self.last_keypress_time = time.time()
        self.update_timer()

    def update_timer(self):
        # Calculate time left
        current_time = time.time()
        elapsed_time = current_time - self.last_keypress_time
        time_left = max(0, self.typing_delay - int(elapsed_time * 1000))

        # Update the timer display
        self.timer_var.set(f"Time left: {(time_left / 1000):.2f} seconds")

        if time_left > 0:
            # Schedule the next update
            self.root.after(100, self.update_timer)
        else:
            # Timer finished
            self.clear_text()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClearApp(root)
    root.mainloop()
