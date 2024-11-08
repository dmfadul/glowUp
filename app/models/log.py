import datetime
from app import db


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
