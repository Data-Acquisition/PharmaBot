from application.models import db

class PharmaInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    adress = db.Column(db.Unicode(128))
    weekTime = db.Column(db.Time)
    weekendTime = db.Column(db.Time)
    geo = db.Column(db.Unicode(64))
    phone = db.Column(db.Integer)
    photo = db.Column(db.Unicode(128))