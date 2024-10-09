from flask import Blueprint, render_template, redirect, url_for, request


contact_bp = Blueprint('contact',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/contact/static')


@contact_bp.route('/contato', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        
        return redirect(url_for('contact.contact'))
    else:
        return render_template('contact.html')