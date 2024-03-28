from flask import Flask, render_template, request, flash
from flask_migrate import Migrate, upgrade
from models import db, User, seed_data
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URI_LOCAL")
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///name.db"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/register", methods = ["GET", "POST"])
def register_new_user():
    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age',type=int)
        email = request.form.get('email')
        username = request.form.get('username')
        phone = request.form.get('phone')

        email_exist = User.query.filter_by(email=email).first()
        username_exist = User.query.filter_by(username=username).first()

        if email_exist or username_exist:
            flash('Username or email already exist!')
        else:
            new_user = User(name=name, age=age, email=email, username=username, phone=phone)
            db.session.add(new_user)
            db.session.commit()
            flash('User created! Welcome!')
    
    return render_template('register_user.html')


@app.route("/allusers")
def all_users():
    users = User.query.all()
    return render_template('users.html', list_of_users=users)

@app.route("/user/<int:user_id>")
def user_page(user_id):
    ...

if __name__ == "__main__":
    with app.app_context():
        upgrade()
        seed_data()
    app.run(debug=True)