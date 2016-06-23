from flask import Blueprint

# a blueprint as a "reusable app"
product = Blueprint('product', __name__)

from . import views
