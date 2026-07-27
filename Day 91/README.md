# 🎧 PDF to Audiobook Converter

A Python script that scans a folder of PDF files, extracts their text, and converts each one into an MP3 audiobook using Google Text-to-Speech (gTTS).

Built as part of the **100 Days of Code** Udemy course assignment.

---

## ✨ Features

- Automatically finds every PDF in the `input_pdfs/` folder — no need to type filenames
- Extracts text page by page using `pypdf`
- Converts extracted text into natural-sounding speech with `gTTS`
- Skips PDFs with no readable text (e.g. scanned image-only PDFs) instead of crashing
- Saves one MP3 per PDF into `output_audio/`, keeping the same filename

---

## 🛠 Built With

- Python 3
- [pypdf](https://pypi.org/project/pypdf/) — PDF text extraction
- [gTTS](https://pypi.org/project/gTTS/) — Google Text-to-Speech (free, no API key required)

---

## ▶️ How to Run

1. Install the required libraries:
   ```bash
   pip install pypdf gtts
   ```
2. Drop one or more PDF files into the `input_pdfs/` folder
3. Run the script:
   ```bash
   python pdf_to_audiobook.py
   ```
4. Find your generated audiobooks in the `output_audio/` folder

**Note:** gTTS requires an internet connection, since it sends text to Google's servers to generate speech.

---

## 📁 Project Structure

```
pdf_to_audiobook/
├── pdf_to_audiobook.py
├── input_pdfs/       ← put your PDFs here
└── output_audio/     ← generated MP3s appear here
```

---

## 🧠 How It Works

1. `extract_text_from_pdf()` opens a PDF with `PdfReader` and loops through every page, collecting all extractable text into a single string. Pages with no extractable text (e.g. scanned images) are skipped with a warning.
2. `convert_text_to_speech()` passes that text to `gTTS`, which generates and saves an MP3 file.
3. `process_all_pdfs()` ties it together: it scans `input_pdfs/` for `.pdf` files, and for each one, extracts the text, converts it to speech, and saves the result in `output_audio/` with a matching filename (e.g. `book.pdf` → `book.mp3`).

---

## 💭 Reflection

*(Fill this in after building — this section is part of the assignment)*

- **How did I approach the project?**
- **What was hard? What was easy?**
- **What would I do differently next time?**
- **Biggest learning from today?**

---

## 📌 Possible Improvements

- Add OCR support (`pytesseract` + `pdf2image`) for scanned/image-based PDFs
- Let the user choose the language/voice via a command-line argument
- Add a progress bar for long PDFs
- Split very long PDFs into multiple shorter MP3 chapters
- Support other TTS engines (e.g. Google Cloud TTS, AWS Polly) for higher-quality voices

---

## 📄 License

Free to use for learning purposes.
