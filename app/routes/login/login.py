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
        
        # Verifica se o usuário existe e se a senha está correta
        if user and user.password == password:
            login_user(user)
            Log.add_entry(f'Usuário {user.id} Logado')
            return redirect(url_for('login.home'))
        else:
            flash("Usuário ou senha inválidos", "danger")  # Mensagem de erro
    
    return render_template('login.html')
