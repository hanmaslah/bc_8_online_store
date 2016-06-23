from flask import render_template
from . import main


@main.route('/')
def index():
    '''
    This leads to the index page.
    The render_template matcher is used to specify that
    a request renders a given template.
    '''
    return render_template('index.html')
