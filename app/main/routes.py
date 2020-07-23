from flask import render_template
from flask_login import login_required

from app.main import bp
from app.main.forms import AddCartridge, RegisterPrinter


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/add_printer')
@login_required
def add_printer():
    form = RegisterPrinter()
    return render_template('add_printer.html', title='Add Printer', form=form)