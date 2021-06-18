from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from os import path
from flask_login import LoginManager
from .config import MYSQL


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "testtesttest"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL['DB_USER']}:{MYSQL['DB_PASSWORD']}@{MYSQL['DB_HOST']}:{MYSQL['DB_PORT']}/{MYSQL['DB_NAME']}"
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://richgunwoo:Qrhksflwk!0909@localhost:3306/travel_mate?charset=utf8'
    db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Blog

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    db.create_all(app=app)
    print('Creating database')
