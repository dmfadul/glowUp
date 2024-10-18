from flask import Blueprint, render_template, redirect, url_for, request


sobre_bp = Blueprint('sobre',
                       __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/sobre/static')


@sobre_bp.route('/sobre', methods=['GET', 'POST'])
def sobre():
    if request.method == 'POST':
        data = request.form
        
        return redirect(url_for('sobre.sobre'))
    else:
        return render_template('sobre.html')