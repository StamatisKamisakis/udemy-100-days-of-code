import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

from color_extractor import extract_top_colors

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join("static", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def is_allowed_file(filename: str) -> bool:
    """Checks the file extension is one we know how to open as an image."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """The upload page."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    """Handles the uploaded image: saves it, extracts colors, shows the result."""
    uploaded_file = request.files.get("image")

    if not uploaded_file or uploaded_file.filename == "":
        return redirect("/")

    if not is_allowed_file(uploaded_file.filename):
        return redirect("/")

    filename = secure_filename(uploaded_file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    uploaded_file.save(filepath)

    colors = extract_top_colors(filepath)
    image_url = "/" + filepath.replace("\\", "/")  # normalize for Windows paths

    return render_template("result.html", colors=colors, image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)
