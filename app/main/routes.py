from flask import flash, redirect, render_template, url_for, current_app
from flask_login import current_user, login_required

from app import db
from app.main import bp
from app.main.forms import AddCartridge, RegisterPrinter
from app.models import User, Printer, Cartridge


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/add_printer', methods=['POST'])
@login_required
def add_printer():
    form = RegisterPrinter()
    if form.validate_on_submit():
        printer = Printer(name=form.name.data, 
                        brand=form.brand.data,
                        model=form.model.data,
                        vendor=form.vendor.data,
                        product_url=form.product_url.data)
        db.session.add(printer)
        db.session.commit()
        flash('You have added {}!'.format(printer.name))
        return redirect(url_for('main.index'))
    return render_template('add_printer.html', title='Add Printer', form=form)

@bp.route('/add_cartridge')
def add_cartridge():
    return render_template('add_cartridge.html')

@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)