from application.models import db
import datetime

class MyModel():
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
  updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc),
                        onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))
