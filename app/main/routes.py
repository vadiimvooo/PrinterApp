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

@bp.route('/add_printer', methods=['GET', 'POST'])
@login_required
def add_printer():
    form = RegisterPrinter()
    if form.validate_on_submit():
        printer = Printer(name=form.name.data, 
                        brand=form.brand.data,
                        model=form.model.data,
                        num_cartridges=form.num_cartridges.data,
                        cart_on_hand=form.cart_on_hand.data,
                        vendor=form.vendor.data,
                        product_url=form.product_url.data,
                        user=current_user)
        db.session.add(printer)
        db.session.commit()
        flash('You have added {}!'.format(printer.name))
        return redirect(url_for('main.index'))
    return render_template('add_printer.html', title='Add Printer', form=form)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@bp.route('/printer/<printer_id>')
@login_required
def printer(printer_id):
    printer = Printer.query.filter_by(id=printer_id).first_or_404()
    return render_template('printer.html', printer=printer)


@bp.route('/printer/<printer_id>/add_cartridge')
@login_required
def add_cartridge(printer_id):
    form = AddCartridge()
    return render_template('add_cartridge.html', form=form)