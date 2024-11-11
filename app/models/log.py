import datetime
from app import db


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    @classmethod
    def add_entry(cls, info):
        log = cls(info=info)
        db.session.add(log)
        db.session.commit()

    @classmethod
    def get_report(cls):
        report = []
        for log in cls.query.all():
            report.append(f"[{log.created_at}]: {log.info}")

        return report