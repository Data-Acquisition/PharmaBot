from application.models import db

class PollRes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, nullable=False)
    namePoll = db.Column(db.Unicode(128), nullable=False)
    ques_and_answ = db.Column(db.Unicode(256), nullable=False)