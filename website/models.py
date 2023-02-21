from sqlalchemy import func

from . import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(5000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    notes = db.relationship('Note')


class Rooms(db.Model):
    __bind__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    roomname = db.Column(db.String(250), unique=True)
    message = db.Column(db.String(50000), default='{"0":""}')
    count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return "('ID:{}', 'roomname:{}', 'count:{}')".format(self.id, self.roomname, self.count)
