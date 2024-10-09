from flask import Blueprint, render_template, redirect, url_for, request


register_bp = Blueprint('register',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/register/static')


@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        
        return redirect(url_for('register.register'))
    else:
        return render_template('register.html')