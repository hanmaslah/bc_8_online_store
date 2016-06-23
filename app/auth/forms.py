from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms import BooleanField, SubmitField, ValidationError, validators
from ..models import Users


class LoginForm(Form):
    '''This class creates a login form
    '''
    # for a login, the username and password are required.
    # remember is the result of the checkbox written
    # 'keep me logged in'
    username = StringField('Username',
                           [validators.Required(
                            message='Kindly Enter your username')]
                           )
    password = PasswordField('Password', [validators.Required()])
    remember = BooleanField('Keep me logged in.')
    submit = SubmitField('Log In')


class RegistrationForm(LoginForm):
    '''This class creates a registration form.
    '''

    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    phone = StringField('Phone Number')
    username = StringField('Username', [validators.Required()])

    password = PasswordField('Password', [validators.Required(),
                                          validators.EqualTo(
        'password_confirmation',
        'Passwords do not match.'
    )])
    # check if Passwords match
    password_confirmation = PasswordField('Password Confirmation',
                                          [validators.Required()])
    submit = SubmitField('Submit')
    remember = None

    def validate_username(self, field):
        '''This method checks if a username already exists in
        the database
        '''
        # check fot the first occurrence of that username and raise an error
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists.')
