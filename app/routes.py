from app import app, login_manager, db, bcrypt
from .models import *
from .forms import *
from flask import request, redirect, render_template, flash
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/", methods=["GET", "POST"])
def index():
    events = Event.query.all()
    return render_template('index.html', events=events, current_user=current_user)


# Login #
@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = CreateUserForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(email=email, username=username, password=bcrypt.generate_password_hash(password).decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect("/")
    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('До новых встреч!')
    return redirect("/")
