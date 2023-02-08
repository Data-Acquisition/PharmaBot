from application.models import db
# from application.models.basemodel import MyModel
import datetime

class Notify(db.Model):
  __tablename__ = 'notify'
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
  updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
  name = db.Column(db.Unicode(64))
  description = db.Column(db.Unicode(256))
  banner = db.Column(db.Unicode(128))