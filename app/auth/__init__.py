from flask import Blueprint

# a blueprint as a "reusable app"
auth = Blueprint('auth', __name__)

from . import views
