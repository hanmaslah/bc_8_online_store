from flask import render_template, redirect, request, url_for, flash
from flask_login import logout_user, login_user
from . import auth
from .. import db
from ..models import Users
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `Users` class
        user = Users.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            user.authenticated = True
            login_user(user, form.remember.data)
            flash('Welcome %s' % user.username)
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
            return redirect(request.args.get('next') or url_for('store.index'))
        # return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password.')
        # if login not successful, return to login page
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
# @login_required
def logout():
    logout_user()
    # flash('You have been logged out.')
    # retuns user to the index page
    return redirect(url_for('main.index'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = Users(form.first_name.data,
                     form.last_name.data,
                     form.username.data,
                     form.password.data,
                     form.phone.data
                     )
        db.session.add(user)
        db.session.commit()

        # after first signup, you will be redirected to the login page
        return redirect(url_for('auth.login'))
        # Render the signup.html from the templates folder
    return render_template('auth/signup.html', form=form)
