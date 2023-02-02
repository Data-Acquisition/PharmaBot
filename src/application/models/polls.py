from application.models import db
from application.models.basemodel import MyModel

class PollInfo(db.Model, MyModel):
    __tablename__ = 'poll_info'
    # id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Unicode(128), nullable=False)
    reward = db.Column(db.Integer)