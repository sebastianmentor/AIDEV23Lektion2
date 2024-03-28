from flask import Flask, render_template, request, flash
from flask_migrate import Migrate, upgrade
from models import db, User
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI_LOCAL")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/register", methods = ["GET", "POST"])
def register_new_user():
    ...

@app.route("/allusers")
def all_users():
    ...

@app.route("/user/<int:user_id>")
def user_page(user_id):
    ...

if __name__ == "__main__":
    with app.app_context():
        upgrade()
    app.run(debug=True)