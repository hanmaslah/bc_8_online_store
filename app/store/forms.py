from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms import SubmitField, validators


class StoreForm(Form):
    '''This class creates an StoreForm
    object.
    '''

    name = StringField('Store',
                       [validators.Required(message='Kindly enter a store.'),
                        validators.Length(
                           max=70,
                           message='Your store name is too long.'
                       )
                       ]
                       )
    description = TextAreaField('Store Description',
                                [validators.required(
                                    message='Please describe your store.')])
    submit = SubmitField('Create Store')

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
