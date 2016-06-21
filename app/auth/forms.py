from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField, ValidationError, validators
from ..models import Users


class LoginForm(RegistrationForm):
    '''This class extends the registration form class
    '''
    username = StringField('Username',
                           [validators.Required(
                            message='Kindly Enter your username')]
                           )
    password = PasswordField('Password', [validators.Required()])
    remember = BooleanField('Keep me logged in.')
    submit = SubmitField('Log In')


class RegistrationForm(Form):
    '''This class creates a registration form.
    '''
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    email = StringField(
        'Email Address',
        [
            validators.Required(),
            validators.Length(
                min=6, max=64, message='Your email is invalid')
        ]
    )
    password = PasswordField('Password', [validators.Required(),
                                          validators.EqualTo(
        'password_confirmation',
        'Passwords do not match.'
    )])
    password_confirmation = PasswordField('Password Confirmation',
                                          [validators.Required()])
    submit = SubmitField('Submit')
    remember = None

    def validate_username(self, field):
        '''This method checks if a username already exists in
        the database
        '''
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists.')
