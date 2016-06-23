from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()

"""
Flask-Login provides user session management for Flask.
It handles the common tasks of logging in, logging out,
and remembering your users’ sessions over extended periods of time.
"""
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    '''
    creates a Flask instance in __init__.py file of my package
    '''
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    toolbar.init_app(app)

    ''' A blueprint defines a collection of views, templates,
 static files and other elements that can be
 applied to an application.
    '''
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .store import store as store_blueprint
    app.register_blueprint(store_blueprint, url_prefix='/store')

    from .products import product as product_blueprint
    app.register_blueprint(product_blueprint, url_prefix='/product')

    return app
