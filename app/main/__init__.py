from flask import Blueprint

# a blueprint as a "reusable app"
main = Blueprint('main', __name__)

from . import views, errors
