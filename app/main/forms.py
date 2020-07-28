from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models import Printer, Cartridge


class RegisterPrinter(FlaskForm):
    name = StringField('Printer Name', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model')
    num_cartridges = IntegerField('Number of Cartridges', validators=[DataRequired()])
    cart_on_hand = IntegerField('Cartridges On Hand', validators=[DataRequired()])
    vendor = StringField('Vendor')
    product_url = StringField('Product URL')
    submit = SubmitField('Register Printer')

class AddCartridge(FlaskForm):
    color = StringField('Color', validators=[DataRequired()])
    model = StringField('Model')
    product_url = StringField('Product URL')
    quantity = IntegerField('Quantity', validators=[DataRequired()])