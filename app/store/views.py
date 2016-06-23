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
    stores records in the database
    specific to a user
    '''
    user = Users.query.filter_by(id=current_user.id).first()
    stores_instance = user.stores.all()
    available_stores = 0
    for i in stores_instance:
        available_stores += 1
    # set the available_stores to length of the stores_instance

# loop through all stores and increment the number of available stores
# renders the index template in the store folder
# passes stores_ as the queried stores
# and available_stores as number of stores
    return render_template('store/index.html', stores_=stores_instance,
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
        user = Users.query.filter_by(id=current_user.id).first()
        stores_instance = Stores(name=form.name.data,
                                 description=form.description.data,
                                 user_id=current_user.id)

        # import ipdb; ipdb.set_trace()
        user.stores.append(stores_instance)
        db.session.add(stores_instance)
        db.session.commit()
        flash('Store added successfully.')
        return redirect(request.args.get('next') or url_for('store.index'))

    user = Users.query.filter_by(id=current_user.id).first()
    user_stores = user.stores.all()
    available_stores = 0
    for i in user_stores:
        available_stores += 1

    return render_template('store/new_store.html',
                           form=form, stores_=user_stores,
                           available_stores=available_stores)
