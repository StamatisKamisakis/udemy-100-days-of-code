from pathlib import Path
import os
import shutil

# Path to the Downloads folder
DOWNLOADS_DIR = Path.home() / "Downloads"

# Dictionary mapping folder names to file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".dmg", ".deb"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".sql"],
}


def organize_downloads():
    # Check if the Downloads directory exists
    if not DOWNLOADS_DIR.exists():
        print(f"Directory {DOWNLOADS_DIR} does not exist.")
        return

    # Iterate through all files in the Downloads folder
    for item in DOWNLOADS_DIR.iterdir():
        # Skip subdirectories, only process files
        if item.is_dir():
            continue

        file_extension = item.suffix.lower()
        moved = False

        # Match file extension to a category
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                # Create category folder if it doesn't exist
                target_folder = DOWNLOADS_DIR / category
                target_folder.mkdir(exist_ok=True)

                destination_path = target_folder / item.name

                # Handle duplicate file names to avoid overwriting
                if destination_path.exists():
                    stem = item.stem
                    destination_path = (
                        target_folder / f"{stem}_copy{file_extension}"
                    )

                # Move file to its respective category folder
                shutil.move(str(item), str(destination_path))
                print(f"Moved: {item.name} -> {category}/")
                moved = True
                break

        # Move unclassified files into an 'Other' folder
        if not moved and file_extension:
            other_folder = DOWNLOADS_DIR / "Other"
            other_folder.mkdir(exist_ok=True)
            destination_path = other_folder / item.name

            if not destination_path.exists():
                shutil.move(str(item), str(destination_path))
                print(f"Moved: {item.name} -> Other/")


if __name__ == "__main__":
    organize_downloads()