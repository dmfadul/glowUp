from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user
from app.models.user import User
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
        
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        password = data.get('password')
        comorbidities = data.get('comorbidities')
        medicines = data.get('medicines')
        allergies = data.get('allergies')
        objectives = data.get('objectives')

        new_user = User.add_entry(name=name,
                                  phone=phone,
                                  email=email,
                                  password=password,
                                  comorbidities=comorbidities,
                                  medicines=medicines,
                                  allergies=allergies,
                                  objectives=objectives
                                  )
        
        return redirect(url_for('register.register'))
    else:
        return render_template('register.html')
    

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
        
        if data.get('password'):
            user.password = data.get('password')

        db.session.commit()
        return redirect(url_for('register.edit_profile'))
    
    return render_template('edit-profile.html', user=user)


@register_bp.route('/profile/delete', methods=['POST'])
@login_required
def delete_profile():
    user = User.query.get(current_user.id)
    user.deactivate()
    logout_user()
    
    return redirect(url_for('register.register'))
