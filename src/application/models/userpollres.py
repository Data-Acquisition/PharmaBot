from application.models import db
from application.models.basemodel import MyModel

class PollRes(db.Model, MyModel):
    # id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('poll_questions.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('poll_answers.id'))