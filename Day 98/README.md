# 📁 Automated Downloads Folder Organizer

A lightweight Python automation script designed to clean up and organize your `Downloads` directory automatically by sorting files into categorized folders based on their extensions.

---

## 🚀 Features

- **Automatic Categorization:** Sorts files into specific folders (`Images`, `Documents`, `Code`, `Archives`, `Executables`, `Audio`, `Video`, `Other`).
- **Safe File Handling:** Prevents file overwriting by appending `_copy` to duplicate filenames in target folders.
- **Cross-Platform Compatibility:** Uses Python's built-in `pathlib` module, making it compatible with Windows, macOS, and Linux out of the box.
- **Zero External Dependencies:** Built entirely with standard Python libraries (`os`, `shutil`, `pathlib`).

---

## 🛠️ Built With

* **Python 3.x**
* `pathlib` (Directory path manipulation)
* `shutil` (File moving operations)
* `os` (Operating system interfaces)

---

## 📂 How It Categorizes Files

| Folder Name | Supported File Extensions |
|---|---|
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.webp`, `.bmp` |
| **Documents** | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| **Audio** | `.mp3`, `.wav`, `.flac`, `.aac` |
| **Video** | `.mp4`, `.mkv`, `.avi`, `.mov` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| **Executables** | `.exe`, `.msi`, `.dmg`, `.deb` |
| **Code** | `.py`, `.js`, `.html`, `.css`, `.json`, `.sql` |
| **Other** | Any other unclassified file extensions |

---

## 🖥️ Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/downloads-organizer.git](https://github.com/YOUR-USERNAME/downloads-organizer.git)
   cd downloads-organizer