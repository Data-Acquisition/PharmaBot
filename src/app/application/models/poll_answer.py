from application.models import db
from application.models.basemodel import MyModel

class Answer(db.Model, MyModel):
  __tablename__ = "poll_answers"
  question_id = db.Column(db.Integer, db.ForeignKey('poll_questions.id'))
  answer = db.Column(db.Unicode(256))
  name_questions = db.relationship('Question', backref=db.backref('answers', lazy='dynamic'))

  def __str__(self) -> str:
      return self.answer