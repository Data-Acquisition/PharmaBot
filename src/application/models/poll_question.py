from application.models import db
from application.models.basemodel import MyModel

class Question(db.Model, MyModel):
  __tablename__ = 'poll_questions'
  poll_id = db.Column(db.Integer, db.ForeignKey("poll_info.id"))
  name_q = db.Column(db.Unicode(128))