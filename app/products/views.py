from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user, session
from . import product
from .. import db
from ..models import Stores, Products, Users
from .forms import ProductForm


@product.route('/home')
@login_required
def index():
    '''This view function displays
    stores records in the database.
    '''
    store = Stores.query.filter_by(user_id=current_user.id).first()
    products_instance = store.products.all()

    available_products = 0
    for i in products_instance:
        available_products += 1
    # import ipdb; ipdb.set_trace()
    return render_template('products/index.html', products_=products_instance,
                           available_products=available_products)


@product.route('/product/<username>/<storeId>')
def store_url(store_username, storeId):
    user = Users.query.filter_by(id=current_user.id)
    store_username = user.username
    store = Stores.query.filter_by(user_id=current_user).first()
    storeId = store.id
    with product.test_request_context():
        return render_template('store/index.html', store_username=store_username, storeId=storeId)


@product.route('/products/new', methods=['GET', 'POST'])
@login_required
def product():
    '''This view function creates a
    new store record and displays
    current user stores.
    '''
    form = ProductForm()
    if form.validate_on_submit():
        # user = Users.query.filter_by(id=current_user.id).first()
        store = Stores.query.filter_by(user_id=current_user.id).first()
        product_instance = Products(name=form.name.data,
                                    description=form.description.data,
                                    store_id=store.id)
        # import ipdb; ipdb.set_trace()
        # store.products.append(product_instance)
        db.session.add(product_instance)
        db.session.commit()
        flash('Product added successfully.')
        return redirect(request.args.get('next') or url_for('product.index'))

    store = Stores.query.filter_by(user_id=current_user.id).first()
    product_stores = store.products.all()
    # product_stores = Products.query.filter_by(store_id=store.id)
    available_products = 0
    for i in product_stores:
        available_products += 1
    return render_template('products/new_product.html',
                           form=form, stores_=product_stores,
                           available_stores=available_products)
