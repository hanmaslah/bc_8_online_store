from flask import render_template, flash
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    flash("Sorry, We couldn't find the page you requested.")
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    flash("Oops, something went wrong.")
    return render_template('500.html'), 500
