from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required


login_bp = Blueprint('login',
                     __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/login/static')


@login_bp.route('/')
def index():
    return redirect(url_for('login.login'))


@login_bp.route('/home')
def home():
    return render_template('home.html')


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)

        
        return redirect(url_for('login.home'))
    
    else:
        return render_template('login.html')