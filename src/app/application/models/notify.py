from application.models import db
from application.models.basemodel import MyModel

class Notify(db.Model, MyModel):
  __tablename__ = 'notify'
  name = db.Column(db.Unicode(64))
  description = db.Column(db.Unicode(256))
  banner = db.Column(db.Unicode(128))