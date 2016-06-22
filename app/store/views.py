from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import store
from .. import db
from ..models import Stores, Users
from .forms import StoreForm


@store.route('/home')
@login_required
def index():
    '''This view function displays
    stores records in the database.
    '''
    stores_ = Stores.query.all()
    available_stores = 0
    # add_store = 0

    for i in stores_:
            available_stores += 1
    return render_template('store/index.html', stores_=stores_,
                           available_stores=available_stores)


@store.route('/me')
def my_store():
    '''This view function displays
    stores records in the database
    specific to a user
    '''
    user = Users.query.filter_by(user_id=current_user.id).first()
    stores_ = user.stores.all()
    available_stores = 0

    for i in stores_:
        if i.already_added:
            available_stores += 1
    return render_template('store/view_store.html',
                           stores_=stores_,
                           available_stores=available_stores)


@store.route('/new', methods=['GET', 'POST'])
@login_required
def store():
    '''This view function creates a
    new store record and displays
    current user stores.
    '''
    form = StoreForm()
    if form.validate_on_submit():
        user = current_user.id
        store_ = Stores(name=form.name.data,
                        description=form.description.data,
                        user_id=user)
        # import ipdb; ipdb.set_trace()
        db.session.add(store_)
        db.session.commit()
        flash('Store added successfully.')
        return redirect(request.args.get('next') or url_for('store_.index'))

    user = Users.query.filter_by(id=current_user.id).first()
    stores_ = user.stores.all()
    available_stores = 0

    for i in stores_:
            available_stores += 1
    return render_template('store/new_store.html',
                           form=form, istores_=stores_,
                           available_stores=available_stores)
