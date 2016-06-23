from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import store
from .. import db
from ..models import Stores
from .forms import StoreForm


@store.route('/home')
@login_required
def index():
    '''This view function displays
    stores records in the database
    specific to a user
    '''
    stores_ = Stores.query.filter_by(user_id=current_user.id)
    available_stores = 0
    # set the available_stores to zero

# loop through all stores and increment the number of available stores
    for i in stores_:
            available_stores += 1
            # renders the index template in the store folder
            # passes stores_ as the queried stores
            # and available_stores as number of stores
    return render_template('store/index.html', stores_=stores_,
                           available_stores=available_stores)


@store.route('/new', methods=['GET', 'POST'])
@login_required
def store():
    '''This view function creates a
    new store record and displays
    current user stores.
    '''
    form = StoreForm()
    if request.method == 'POST' and form.validate_on_submit():
        store_ = Stores(name=form.name.data,
                        description=form.description.data,
                        user_id=current_user.id)
        # import ipdb; ipdb.set_trace()
        db.session.add(store_)
        db.session.commit()
        flash('Store added successfully.')
        return redirect(request.args.get('next') or url_for('store.index'))

    
    stores_ = Stores.query.filter_by(user_id=current_user.id)
    available_stores = 0

    for i in stores_:
            available_stores += 1
    return render_template('store/new_store.html',
                           form=form, istores_=stores_,
                           available_stores=available_stores)
