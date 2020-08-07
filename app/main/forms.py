from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterPrinter(FlaskForm):
    name = StringField('Printer Name *', validators=[DataRequired()])
    brand = StringField('Brand *', validators=[DataRequired()])
    model = StringField('Model')
    num_cartridges = IntegerField('Number of Cartridges *',
                                  validators=[DataRequired()])
    vendor = StringField('Vendor')
    product_url = StringField('Product URL')
    submit = SubmitField('Register Printer')


class AddCartridge(FlaskForm):
    color = StringField('Color *', validators=[DataRequired()])
    brand = StringField('Brand *', validators=[DataRequired()])
    model = StringField('Model *', validators=[DataRequired()])
    vendor = StringField('Vendor')
    product_url = StringField('Product URL')
    quantity = IntegerField('Starting Quantity *',
                            validators=[DataRequired()],
                            render_kw={
                                "placeholder":
                                    "How many extra cartridges do you have?"
                                })
    submit = SubmitField('Add Cartridge')


class EditPrinter(FlaskForm):
    name = StringField('Printer Name')
    brand = StringField('Brand')
    model = StringField('Model')
    num_cartridges = StringField('Number of Cartridges')
    vendor = StringField('Vendor')
    product_url = StringField('Product URL')
    submit = SubmitField('Submit')


class EditCartridge(FlaskForm):
    color = StringField('Color')
    brand = StringField('Brand')
    model = StringField('Model')
    vendor = StringField('Vendor')
    product_url = StringField('Product URL')
    quantity = IntegerField('Quantity')
    submit = SubmitField('Submit')


class Delete(FlaskForm):
    submit = SubmitField('Delete')
