# 🎨 Image Colour Palette Generator

A Flask website that finds the 10 most common colours in any uploaded image, using NumPy for the analysis — inspired by [Flat UI Colors](https://flatuicolors.com).

Built as part of the **100 Days of Code** Udemy course assignment (Day 92).

---

## ✨ Features

- Upload any image (JPG, PNG, WEBP, BMP)
- Analyzes every pixel using NumPy to find the 10 most dominant colours
- Groups similar shades together ("bucketing") so results are meaningful, not thousands of near-identical tones
- Shows each colour's hex code and what percentage of the image it covers
- Click any swatch to copy its hex code to the clipboard

---

## 🛠 Built With

- Python 3 + Flask
- NumPy — for the actual colour-counting logic
- Pillow (PIL) — for opening/resizing images

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install flask numpy pillow
   ```
2. Run the app:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000` in your browser

---

## 📁 Project Structure

```
color_palette_generator/
├── app.py                  ← Flask routes (upload handling)
├── color_extractor.py      ← NumPy colour-extraction logic
├── templates/
│   ├── index.html          ← upload page
│   └── result.html         ← results page
└── static/
    ├── css/style.css
    └── uploads/             ← uploaded images are temporarily stored here
```

---

## 🧠 How It Works

1. The user uploads an image via a form on `index.html`.
2. `app.py` saves the image and passes it to `extract_top_colors()` in `color_extractor.py`.
3. The image is converted into a NumPy array of RGB pixel values.
4. Similar colours are grouped together by rounding each RGB value to the nearest "bucket" (e.g. steps of 32) — without this, near-identical shades (like two barely-different blues) would be counted as separate colours, and the "top 10" would just be ten near-identical tones instead of ten *visually distinct* colours.
5. `np.unique()` counts how often each bucketed colour appears, and the 10 most frequent are converted into hex codes and percentages.
6. `result.html` displays each colour as a clickable swatch.

---

## 💭 Reflection

*(Fill this in after building — this section is part of the assignment)*

- **How did I approach the project?**
- **What was hard? What was easy?**
- **What would I do differently next time?**
- **Biggest learning from today?**

---

## 📌 Possible Improvements

- Let the user choose how many colours to extract (not just top 10)
- Adjustable bucket size (finer vs coarser colour grouping)
- Drag-and-drop upload instead of a plain file picker
- Export the palette as a downloadable image or CSS variables file

---

## 📄 License

Free to use for learning purposes.
