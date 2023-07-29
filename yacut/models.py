import random
import string

from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @classmethod
    def generate_short_url(cls):
        while True:
            short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            if URLMap.query.filter_by(short=short).first() is None:
                break
        return short

    @staticmethod
    def get_full_link(short_link):
        return 'http://localhost/' + short_link

    def to_dict(self):
        return {
            'url': self.original,
            'short_link': self.get_full_link(self.short)
        }
