import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1. Find the absolute path of the directory where main.py is located
base_dir = os.path.abspath(os.path.dirname(__file__))

# 2. Build the path to the database
db_path = os.path.join(base_dir, "instance", "cafes.db")

# 3. PRINT FOR DEBUGGING (Look at your terminal output!)
print("\n" + "="*50)
print(f"Looking for database at: {db_path}")
print(f"Does the file exist there? -> {os.path.exists(db_path)}")
print("="*50 + "\n")

# 4. Set up the URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    __tablename__ = 'cafe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

# Route 1: Home Page - Fetch and display all cafes
@app.route("/")
def home():

    # Fetch all records from the cafe table, ordered by name
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()

    # Render the index.html template and pass the list of cafes
    return render_template("index.html", cafes=all_cafes)

# Route 2: Add a new cafe
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        # take the form data and create a new Cafe object
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")

if __name__ == '__main__':
    # Create the database tables if they don't exist yet
    with app.app_context():
        db.create_all()
        
    app.run(debug=False)