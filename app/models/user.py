from app import db
from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.Text, nullable=False)
    comorbidities = db.Column(db.Text, nullable=True)
    medicines = db.Column(db.Text, nullable=True)
    allergies = db.Column(db.Text, nullable=True)
    objectives = db.Column(db.Text, nullable=True)

    @classmethod
    def add_entry(cls,
                  name,
                  phone,
                  email,
                  password,
                  comorbidities,
                  medicines,
                  allergies,
                  objectives,
                  is_admin=None):
        user = cls(name=name,
                   phone=phone,
                   email=email,
                   is_admin=is_admin if is_admin else False,
                   password=password,
                   comorbidities=comorbidities,
                   medicines=medicines,
                   allergies=allergies,
                   objectives=objectives)
        db.session.add(user)
        db.session.commit()
        return user

    def activate(self):
        self.is_active = True
        db.session.commit()
    
    def deactivate(self):
        self.is_active = False
        db.session.commit()

    @classmethod
    def gen_report(cls):
        users = cls.query.all()

        output = []
        for user in users:
            if not user.is_active:
                continue

            output.append([
                user.name,
                user.phone,
                user.email,
                user.comorbidities,
                user.medicines,
                user.allergies,
                user.objectives
            ])

        return output