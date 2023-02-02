from application.models import db
from application.models.basemodel import MyModel

class PharmaInfo(db.Model, MyModel):
    __tablename__ = 'pharma_info'
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    address = db.Column(db.Unicode(128))
    week_time = db.Column(db.Time)
    weekend_time = db.Column(db.Time)
    latitude = db.Column(db.Unicode(128))
    longitude = db.Column(db.Unicode(128))
    phone = db.Column(db.Integer)
    photo = db.Column(db.Unicode(128))