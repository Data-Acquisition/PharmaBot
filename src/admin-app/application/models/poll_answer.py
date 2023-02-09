# from application.models import db
# import datetime

# class Answer(db.Model):
#   __tablename__ = "poll_answers"
#   id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
#   created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
#   updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
#                         onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
#   question_id = db.Column(db.Integer, db.ForeignKey('poll_question.id'))
#   answer = db.Column(db.Unicode(256))