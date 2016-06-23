from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import product
from .. import db
from ..models import Stores, Users, Products
from .forms import ProductForm


@product.route('/product')
@login_required
def index():
    '''This view function displays
    stores records in the database.
    '''
    products_ = Products.query.all()
    available_products = 0
    # add_store = 0

    for i in products_:
        available_products += 1
    return render_template('products/index.html', products_=products_,
                           available_products=available_products)


@product.route('/products/new', methods=['GET', 'POST'])
@login_required
def product():
    '''This view function creates a
    new store record and displays
    current user stores.
    '''
    form = ProductForm()
    if form.validate_on_submit():
        store = Stores.store.id
        product_ = Products(name=form.name.data,
                            description=form.description.data,
                            store_id=store)
        # import ipdb; ipdb.set_trace()
        db.session.add(product_)
        db.session.commit()
        flash('Product added successfully.')
        return redirect(request.args.get('next') or url_for('product_.index'))

    user = Users.query.filter_by(id=current_user.id).first()
    stores_ = user.stores.all()
    available_stores = 0

    for i in stores_:
        if i.already_added:
            available_stores += 1
    return render_template('product/new_product.html',
                           form=form, stores_=stores_,
                           available_stores=available_stores)
