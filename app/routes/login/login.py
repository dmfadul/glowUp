from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Log



login_bp = Blueprint('login',
                     __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/login/static')


@login_bp.route('/')
def index():
    return redirect(url_for('login.login'))


@login_bp.route('/home')
@login_required
def home():
    return render_template('home.html')


@login_bp.route('/logout')
def logout():
    Log.add_entry(f'Usuário {current_user.id} Deslogado')
    logout_user()
    return redirect(url_for('login.login'))


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login.home'))
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Login ou Senha Inválido", "danger")
            return redirect(url_for('login.login'))
        
        password_is_correct = user.password == password
        if not user or not password_is_correct:
            flash("Login ou Senha Inválido", "danger")
            return redirect(url_for('login.login'))

        login_user(user)
        Log.add_entry(f'Usuário {user.id} Logado')
        return redirect(url_for('login.home'))
    
    else:
        return render_template('login.html')