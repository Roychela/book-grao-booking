from app import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username=db.Column(db.String(255), nullable=False,unique=True)
    fullname=db.Column(db.String(255),nullable=False)
    password_hash = db.Column(db.String(255))
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}{self.fullname}'



class Room(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    roomName=db.Column(db.String(255), nullable=False)
    telephone=db.Column(db.Boolean,nullable=False)
    projector=db.Column(db.Boolean,nullable=False)
    whiteboard=db.Column(db.Boolean,nullable=False)
    cost=db.Column(db.Integer, nullable=False)
    meetings=db.relationship('Booking',backref='room',lazy='dynamic')
    
    def __repr__(self):
        return f'Room {self.roomName}'

class Booking(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title=db.Column(db.String(255),nullable=False,unique=True)
    roomId=db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    bookerId=db.Column(db.Integer, db.ForeignKey('user.id'))
    date=db.Column(db.DateTime,nullable=False)
    startTime=db.Column(db.Integer,nullable=False)
    endTime=db.Column(db.Integer,nullable=False) # should be calculated with startTime and duration
    duration=db.Column(db.Integer,nullable=False)
    #cost=db.Column(db.Integer,nullable=False)
    #participant_users=db.relationship('Participants_user',backref='meeting')
    #participant_partners=db.relationship('Participants_partner',backref='meeting')

    def __repr__(self):
        return f'Meeting {self.id} for {self.id} last for {self.duration}'

