from flask import render_template, url_for, flash, redirect, request
from flaskforum import app, db, bcrypt
from flaskforum.forms import RegistrationForm, LoginForm, TopicForm
from flaskforum.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


topic = [
    {
        'name_topic': 'Post 1',
        'date_posted': 'Augus 20, 2021',
        'content': 'First post content',
    },
    {
        'name_topic': 'Post 2',
        'date_posted': 'March 21, 2021',
        'content': 'Second post content',
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=topic)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            # next_page = request.args.get('next')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/topic", methods=['GET', 'POST'])
@login_required
def create_topic():
    form = TopicForm()
    if form.validate_on_submit():
        topic = Topic(title=form.title.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!')
        return redirect(url_for('home'))
    return render_template('new_topic.html', form = form)