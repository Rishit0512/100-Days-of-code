import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark Application")
        
        # Set the window size to be larger
        self.root.geometry("600x400")  # Width x Height
        
        self.image = None
        self.photo = None

        # Load Button
        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        # Add Watermark Button
        self.watermark_button = tk.Button(root, text="Add Watermark", command=self.add_watermark, state=tk.DISABLED)
        self.watermark_button.pack(pady=10)

        # Save Button
        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        # Label to display image
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image = Image.open(file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.watermark_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.DISABLED)
    
    def add_watermark(self):
        if self.image:
            # Create a copy of the image to avoid modifying the original
            watermarked_image = self.image.copy()
            draw = ImageDraw.Draw(watermarked_image)

            # Define watermark text and position
            text = "Watermark"
            font_size = 36
            try:
                # Use a built-in font with a size of 36
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                # Fallback to the default font if "arial.ttf" is not available
                font = ImageFont.load_default()
                font_size = 20  # Adjusted size for the default font

            # Determine text size and position
            if font_size > 20:
                text_bbox = draw.textbbox((0, 0), text, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
            else:
                text_width, text_height = draw.textsize(text, font=font)

            width, height = watermarked_image.size
            x = width - text_width - 10
            y = height - text_height - 10

            # Apply watermark with black color
            draw.text((x, y), text, font=font, fill=(0, 0, 0, 128))  # Black color with some transparency

            self.image = watermarked_image
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            self.save_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", "Watermark added successfully!")

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
            if file_path:
                self.image.save(file_path)
                messagebox.showinfo("Success", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
