from application.models import db
from application.models.basemodel import MyModel
from flask_login import UserMixin

class User(db.Model, MyModel, UserMixin):
    __tablename__ = 'users'
    # id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255), nullable=False)
    patronymic = db.Column(db.String(255))
    sex = db.Column(db.Integer)
    birthDate = db.Column(db.Date)
    password = db.Column(db.String(255), nullable=False)