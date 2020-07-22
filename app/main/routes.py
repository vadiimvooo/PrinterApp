from flask import render_template

from app.main.forms import LoginForm
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form=form)