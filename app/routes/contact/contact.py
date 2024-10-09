from flask import Blueprint, render_template, redirect, url_for, request


contact_bp = Blueprint('contact',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/contact/static')


@contact_bp.route('/contato')
def contact():
    return render_template('contact.html')