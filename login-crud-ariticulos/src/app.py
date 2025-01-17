from flask import Flask, render_template, request, redirect, url_for, flash, blueprints

from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config

# rutas
from routes.show import show
from routes.crud import crud
from utils.db import db

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()


login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form["username"], request.form["password"])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("crud.mostrar"))
            else:
                flash("Invalid password...")
                return render_template("auth/login.html")
        else:
            flash("User not found...")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/protected")
@login_required
def protected():
    return "Protected route"


app.register_blueprint(show)
app.register_blueprint(crud)


def status_401(error):
    return redirect(url_for("login"))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == "__main__":
    app.config.from_object(config["development"])
    db.init_app(app)
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
