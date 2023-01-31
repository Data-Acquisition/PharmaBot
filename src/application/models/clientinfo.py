from application.models import db

class ClientInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, nullable=False)
    last_name = db.Column(db.String(255))
    first_name = db.Column(db.String(255), nullable=False)
    patronymic = db.Column(db.String(255))
    sex = db.Column(db.Integer)
    birthDate = db.Column(db.Date)
    password = db.Column(db.String(255), nullable=False)
    pollResult = db.Column(db.Unicode(128))