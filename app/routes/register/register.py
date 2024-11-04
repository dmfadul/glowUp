from flask import Blueprint, render_template, redirect, url_for, request
from app.models.user import User


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