from flask import Blueprint, render_template, redirect, url_for, request


services_bp = Blueprint('services',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/services/static')


@services_bp.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        data = request.form
        
        return redirect(url_for('services.services'))
    else:
        return render_template('services.html')