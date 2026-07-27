"""
PDF to Audiobook Converter
---------------------------
Scans the 'input_pdfs' folder for PDF files, extracts their text,
and converts each one into an MP3 audiobook saved in 'output_audio'.

Requirements (install once):
    pip install pypdf gtts
"""

import os
from pypdf import PdfReader
from gtts import gTTS

# ---------- SETTINGS ----------
INPUT_FOLDER = "input_pdfs"
OUTPUT_FOLDER = "output_audio"
LANGUAGE = "en"  # e.g. "en" for English


def extract_text_from_pdf(pdf_path: str) -> str:
    """Reads a PDF file and returns all its text as a single string."""
    reader = PdfReader(pdf_path)
    full_text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()
        if page_text:  # some pages might have no extractable text (e.g. scanned images)
            full_text += page_text + "\n"
        else:
            print(f"  ⚠ Page {page_number} had no extractable text (might be a scanned image).")

    return full_text


def convert_text_to_speech(text: str, output_path: str):
    """Converts text into an MP3 file using gTTS."""
    speech = gTTS(text=text, lang=LANGUAGE, slow=False)
    speech.save(output_path)


def process_all_pdfs():
    """Finds every PDF in the input folder and converts it to an MP3."""
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in '{INPUT_FOLDER}'. Add some PDFs and run again.")
        return

    for filename in pdf_files:
        pdf_path = os.path.join(INPUT_FOLDER, filename)
        print(f"\nProcessing: {filename}")

        text = extract_text_from_pdf(pdf_path)

        if not text.strip():
            print(f"  ✗ Skipped '{filename}' — no readable text found.")
            continue

        output_filename = os.path.splitext(filename)[0] + ".mp3"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        print(f"  Converting text to speech... ({len(text)} characters)")
        convert_text_to_speech(text, output_path)
        print(f"  ✓ Saved audiobook: {output_path}")


if __name__ == "__main__":
    process_all_pdfs()
