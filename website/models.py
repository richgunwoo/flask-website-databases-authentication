from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'test_users'
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum("active", "deleted", "blocked"), default="active")
    email = db.Column(db.String(length=255), nullable=True)
    password = db.Column(db.String(length=2000), nullable=True)
    name = db.Column(db.String(length=255), nullable=True)
    create_at = db.Column(db.DateTime(timezone=True), default=db.func.now())

    blogs = db.relationship('Blog')
    

class Blog(db.Model):
    __tablename__ = 'test_blogs'

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(length=255), nullable=True)
    body = db.Column(db.String(length=2000), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('test_users.id'))