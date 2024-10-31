from app import db
from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(100), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.Text, nullable=False)

    @classmethod
    def add_entry(cls, username, password):
        user = cls(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user
