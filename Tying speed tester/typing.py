import tkinter as tk
from tkinter import messagebox, font
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("500x300")       
        self.root.configure(bg="#87CEEB")  # Sky blue background

        # List of sample texts
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Pack my box with five dozen liquor jugs.",
            "How razorback-jumping frogs can level six piqued gymnasts!",
            "The five boxing wizards jump quickly.",
            "Jinxed wizards pluck ivy from the big quilt."
        ]

        self.sample_text = random.choice(self.sample_texts)  # Randomly select a sample text
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        # Define custom fonts
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        sample_font = font.Font(family="Arial", size=12)
        text_font = font.Font(family="Courier New", size=12)
        button_font = font.Font(family="Helvetica", size=12, weight="bold")

        # Title Label
        self.title_label = tk.Label(self.root, text="Typing Speed Test", font=title_font, bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Sample Text Label
        self.sample_text_label = tk.Label(self.root, text=self.sample_text, font=sample_font, bg="#f0f0f0", wraplength=450, justify="left")
        self.sample_text_label.pack(pady=10)

        # Text Entry
        self.text_entry = tk.Text(self.root, height=5, width=60, font=text_font, wrap="word", bd=2, relief="solid")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_timer)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", font=button_font, bg="#4CAF50", fg="white", relief="raised", command=self.calculate_speed)
        self.submit_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showinfo("Info", "You need to start typing first!")
            return

        typed_text = self.text_entry.get("1.0", "end-1c").strip()
        elapsed_time = time.time() - self.start_time

        # Calculate words per minute (WPM)
        words = len(typed_text.split())
        wpm = (words / (elapsed_time / 60))

        # Display result
        messagebox.showinfo("Typing Speed", f"You typed {words} words in {elapsed_time:.2f} seconds.\nTyping Speed: {wpm:.2f} WPM")

        # Reset the timer and sample text for the next test
        self.start_time = None
        self.text_entry.delete("1.0", "end")
        self.sample_text = random.choice(self.sample_texts)  # Select a new random sample text
        self.sample_text_label.config(text=self.sample_text)  # Update the sample text label

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()


