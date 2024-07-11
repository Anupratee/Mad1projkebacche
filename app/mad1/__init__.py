from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from os import path
from mad1.models import DB_NAME, db, User

def create_app():
    app = Flask(__name__) #initializing flask instance
    app.config['SECRET_KEY'] = 'mad1'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    app.static_folder = "static"

    with app.app_context():
        if not path.exists('mad1/instance' + DB_NAME):
            db.create_all()
            print("Created db")

    app.app_context().push()

    from mad1.auth import auth

    app.register_blueprint(auth, url_prefix = "/")

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" #redirect to login page
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app




