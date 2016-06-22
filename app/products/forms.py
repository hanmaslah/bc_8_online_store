from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms import SubmitField, validators


class ProductForm(Form):
    '''This class creates an ProductForm
    object.
    '''
# a store has a name and a description
    name = StringField('Product',
                       [validators.Required(message='Kindly enter a product.'),
                        validators.Length(
                           max=70,
                           message='Your product name is too long.'
                       )
                       ]
                       )
    unit_price = StringField('Unit Price',
                             [validators.required(
                                    message='Please enter the unit price.')])
    description = TextAreaField('Product Description',
                                [validators.required(
                                    message='Please describe your product.')])
    submit = SubmitField('Add Product')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
