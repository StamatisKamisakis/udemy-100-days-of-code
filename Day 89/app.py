from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    """A single task in our list."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), default="General")
    priority = db.Column(db.String(20), default="Medium")  # Low / Medium / High
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


# Display order for priority: High first, then Medium, then Low
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


@app.route("/")
def index():
    # Category filter via query param: /?category=Work
    selected_category = request.args.get("category", "All")

    query = Todo.query
    if selected_category != "All":
        query = query.filter_by(category=selected_category)

    todos = query.all()
    # Sort: incomplete tasks first, then by priority
    todos.sort(key=lambda t: (t.done, PRIORITY_ORDER.get(t.priority, 1)))

    # Unique categories for the filter dropdown
    all_categories = sorted({t.category for t in Todo.query.all()})

    return render_template(
        "index.html",
        todos=todos,
        all_categories=all_categories,
        selected_category=selected_category,
    )


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "").strip() or "General"
    priority = request.form.get("priority", "Medium")

    if title:  # don't add empty tasks
        new_todo = Todo(title=title, category=category, priority=priority)
        db.session.add(new_todo)
        db.session.commit()

    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
