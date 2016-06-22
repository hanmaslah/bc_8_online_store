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
        if i.already_added():
            available_products += 1
    return render_template('products/index.html', products_=products_,
                           available_products=available_products)


@product.route('/products/already_added', methods=['GET', 'POST'])
@login_required
def already_added():
    if request.method == 'POST':
        id_ = request.form.get('cl')
        product = Products.query.filter_by(id=id_).first()
        product.already_added = True
        db.session.add(product)
        db.session.commit()
        return redirect(request.args.get('next') or url_for('product.index'))


@product.route('/product/me')
@login_required
def my_store_products():
    '''This view function displays
    stores records in the database
    specific to a store
    '''
    store = Stores.query.filter_by(id=current_user.id).first()
    products_ = store.products.all()
    available_products = 0

    for i in products_:
        if i.already_added:
            available_products += 1
    return render_template('products/index.html',
                           iproducts_=products_,
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
        db.session.add(store_)
        db.session.commit()
        flash('Store added successfully.')
        return redirect(request.args.get('next') or url_for('product_.index'))

    user = Users.query.filter_by(id=current_user.id).first()
    stores_ = user.stores.all()
    available_stores = 0

    for i in stores_:
        if i.already_added:
            available_stores += 1
    return render_template('product/new_product.html',
                           form=form, istores_=stores_,
                           available_stores=available_stores)
