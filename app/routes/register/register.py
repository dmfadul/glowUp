from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_required, logout_user, current_user
from app.models import User, Log
from app import db

register_bp = Blueprint('register',
                        __name__,
                        template_folder='templates',
                        static_folder='static',
                        static_url_path='/register/static')

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form

        email = data.get('email')
        # Verificar se o email já está registrado
        if User.query.filter_by(email=email).first():
            flash("Este email já está registrado. Por favor, use outro email.", "error")
            return redirect(url_for('register.register'))

        # Coletar e criar novo usuário
        new_user = User.add_entry(
            name=data.get('name'),
            phone=data.get('phone'),
            email=email,
            password=data.get('password'),
            comorbidities=data.get('comorbidities'),
            medicines=data.get('medicines'),
            allergies=data.get('allergies'),
            objectives=data.get('objectives')
        )

        Log.add_entry(f'Usuário {new_user.id} Cadastrado')
        return redirect(url_for('login.login'))
    
    return render_template('register.html')

@register_bp.route('/check-email')
def check_email():
    email = request.args.get('email')
    exists = User.query.filter_by(email=email).first() is not None
    return jsonify({"exists": exists})

@register_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user = User.query.get(current_user.id)

    if request.method == 'POST':
        data = request.form
        user.name = data.get('name')
        user.phone = data.get('phone')
        user.email = data.get('email')
        user.comorbidities = data.get('comorbidities')
        user.medicines = data.get('medicines')
        user.allergies = data.get('allergies')
        user.objectives = data.get('objectives')

        # Atualizar senha, se fornecida
        if data.get('password'):
            user.password = data.get('password')

        db.session.commit()
        Log.add_entry(f'Usuário {user.id} Atualizado')
        flash("Perfil atualizado com sucesso!", "success")
        return redirect(url_for('register.edit_profile'))
    
    return render_template('edit-profile.html', user=user)

@register_bp.route('/profile/delete', methods=['POST'])
@login_required
def delete_profile():
    user = User.query.get(current_user.id)
    user.deactivate()
    logout_user()
    Log.add_entry(f'Usuário {user.id} Deletado')
    flash("Perfil deletado com sucesso.", "success")
    return redirect(url_for('register.register'))
