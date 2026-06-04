# 🖼️ Day 85: Desktop Watermarking Application

An automated desktop GUI application built with Python that allows users to upload an image and overlay a custom text watermark. This tool eliminates the need for heavy photo editing software like Photoshop when doing repetitive watermarking for social media branding or copyright protection.

---

## 📸 Application Demo

![Application Preview](Day%2085.mp4)

*(Note: If you convert your video to a GIF later, you can change this line to `![Application Preview](Day%2085.gif)`)*

---

## ✨ Features

*   **User-Friendly GUI:** Built with Tkinter for a clean desktop interface.
*   **Image File Filtering:** File dialog restricts selection to popular image formats (`.jpg`, `.png`, `.webp`, etc.).
*   **Live Preview:** Automatically resizes and displays a scaled down version of the uploaded image inside the application while keeping its original aspect ratio.
*   **Dynamic Font Resizing:** Automatically calculates the optimal font size based on the uploaded image's resolution, ensuring the watermark is perfectly legible whether it is a small screenshot or a 4K photograph.
*   **Corner Placement:** Automatically anchors the text near the bottom-right corner with balanced safety padding.
*   **Error Prevention:** Built-in validation checks to ensure fields are not left blank and code execution remains stable.

---

## 🛠️ Core Libraries Used

*   **Tkinter:** For rendering the Graphical User Interface (GUI) windows and managing click events.
*   **Pillow (PIL):** For safe background image streaming, text drawing operations, canvas bounds measurement, and file compression/saving.

---

## 💻 Setup & Local Execution

To run this desktop application on your computer, ensure you have Python installed and execute the following commands inside this folder:

1. **Install the image processing library:**
   ```bash
   pip install pillow
   ```

2. **Launch the application:**
   ```bash
   python main.py
   ```
