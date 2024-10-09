from flask import Blueprint, render_template, redirect, url_for, request


premium_bp = Blueprint('premium',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/premium/static')


@premium_bp.route('/premium', methods=['GET', 'POST'])
def premium():
    if request.method == 'POST':
        data = request.form
        
        return redirect(url_for('premium.premium'))
    else:
        return render_template('premium.html')