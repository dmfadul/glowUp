from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# login_manager = LoginManager()

def create_app():
    config_filename = '../instance/config.py'

    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db.init_app(app)
    
    # login_manager.init_app(app)
    # login_manager.login_view = 'login.login'
    # login_manager.login_message = 'Please log in to access this page.'
    # login_manager.login_message_category = 'danger'
    
    from app.routes.login.login import login_bp
    from app.routes.contact.contact import contact_bp
    from app.routes.register.register import register_bp
    from app.routes.premium.premium import premium_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(premium_bp)
    
    


    return app


create_app()