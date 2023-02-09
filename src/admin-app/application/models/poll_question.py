# from application.models import db
# import datetime

# class Question(db.Model):
#   __tablename__ = 'poll_questions'
#   id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
#   created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
#   updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
#                         onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
#   poll_id = db.Column(db.Integer, db.ForeignKey("poll_info.id"))
#   name_q = db.Column(db.Unicode(128))
#   answers = db.relationship('Answer', backref='poll_questions', lazy='dynamic')
  