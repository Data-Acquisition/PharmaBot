from application.models import db
# from application.models.basemodel import MyModel
import datetime

class PharmaInfo(db.Model):
    __tablename__ = 'pharma_info'
    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
    name = db.Column(db.Unicode(64))
    address = db.Column(db.Unicode(128))
    week_time = db.Column(db.Unicode(128))
    weekend_time = db.Column(db.Unicode(128))
    latitude = db.Column(db.Unicode(128))
    longitude = db.Column(db.Unicode(128))
    phone = db.Column(db.Integer)
    photo = db.Column(db.Unicode(128))