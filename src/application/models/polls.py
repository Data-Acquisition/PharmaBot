from application.models import db

class PollInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    type = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Unicode(128), nullable=False)
    reward = db.Column(db.Integer)
    question = db.Column(db.Unicode(128), nullable=False)
    answer = db.Column(db.Unicode(64), nullable=False)