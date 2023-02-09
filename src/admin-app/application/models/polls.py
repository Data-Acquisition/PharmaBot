from application.models import db
import datetime

class PollInfo(db.Model):
  __tablename__ = 'poll_info'
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
  updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                      onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
  # id = db.Column(db.Integer, primary_key=True)r
  type = db.Column(db.Integer, nullable=False)
  name = db.Column(db.Unicode(128), nullable=False)
  reward = db.Column(db.Integer)
  # questions = db.relationship('Question', backref=db.backref('polls', lazy='dynamic'))
  
  def __str__(self):
        return self.name
  
  
class Question(db.Model):
  __tablename__ = 'poll_questions'
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
  updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
  poll_id = db.Column(db.Integer, db.ForeignKey("poll_info.id"))
  name_q = db.Column(db.Unicode(128))
  name_polls = db.relationship('PollInfo', backref=db.backref('questions', lazy='dynamic'))
  # answers = db.relationship('Answer', backref='poll_questions', lazy='dynamic')
  def __str__(self):
        return self.name_q
  
  
class Answer(db.Model):
  __tablename__ = "poll_answers"
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
  updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
  question_id = db.Column(db.Integer, db.ForeignKey('poll_questions.id'))
  answer = db.Column(db.Unicode(256))
  name_questions = db.relationship('Question', backref=db.backref('answers', lazy='dynamic'))

  def __str__(self) -> str:
      return self.answer