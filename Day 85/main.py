import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Desktop Watermark Application")
        self.root.geometry("500x520")#
        self.root.config(padx=100, pady=100)#padx=20, pady=20

        self.image_path = None
        self.original_image = None

        # --- UI Elements ---
        # Button to upload image
        self.upload_btn = tk.Button(text="1. Select Image", command=self.upload_image, font=("Arial", 12, "bold"))
        self.upload_btn.pack(pady=10)

        # Label for text input
        self.label_text = tk.Label(text="2. Enter Watermark Text:", font=("Arial", 10))
        self.label_text.pack(pady=5)

        # Entry for watermark text
        self.text_entry = tk.Entry(width=30, font=("Arial", 12))
        self.text_entry.insert(0, "© MyWebsite.com")
        self.text_entry.pack(pady=5)

        # Button to apply watermark and save
        self.watermark_btn = tk.Button(text="3. Add Watermark & Save", command=self.add_watermark, font=("Arial", 12, "bold"), bg="#2ecc71", fg="white")
        self.watermark_btn.pack(pady=20)

        # Preview Label
        self.preview_label = tk.Label(text="No image selected")
        self.preview_label.pack(pady=10)

    def upload_image(self):
        # Open file dialog to choose an image
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
        )
        
        if self.image_path:
            # Open and create a small preview for the UI
            self.original_image = Image.open(self.image_path)
            
            # Resize for preview without destroying aspect ratio
            preview_img = self.original_image.copy()
            preview_img.thumbnail((250, 250))
            
            img_tk = ImageTk.PhotoImage(preview_img)
            self.preview_label.config(image=img_tk, text="")
            self.preview_label.image = img_tk  # Keep a reference to avoid garbage collection

    def add_watermark(self):
        if not self.original_image:
            messagebox.showwarning("Warning", "Please select an image first!")
            return

        watermark_text = self.text_entry.get()
        if not watermark_text:
            messagebox.showwarning("Warning", "Watermark text cannot be empty!")
            return

        # Create a copy of the original image to modify
        watermarked_image = self.original_image.copy()
        draw = ImageDraw.Draw(watermarked_image)

        # Configure font size based on image width (dynamic sizing)
        width, height = watermarked_image.size
        font_size = int(width / 20)  # Adjust size dynamically based on image resolution
        
        try:
            # Using default system font with dynamic sizing
            font = ImageFont.load_default(size=font_size)
        except AttributeError:
            # Fallback for older Pillow versions
            font = ImageFont.load_default()

        # Position text at the bottom-right corner with some padding
        # textbbox returns (left, top, right, bottom)
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = width - text_width - 20
        y = height - text_height - 20

        # Draw the text (White color with solid opacity)
        draw.text((x, y), watermark_text, fill=(255, 255, 255), font=font)

        # Open Save File Dialog
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")]
        )

        if save_path:
            watermarked_image.save(save_path)
            messagebox.showinfo("Success", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
