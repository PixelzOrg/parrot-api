from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    container_client_id = db.Column(db.String(255), unique=True, nullable=True)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('videos', lazy=True))
    video_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    video_length = db.Column(db.Integer, nullable=False)
    transcript = db.Column(db.String)  # Use String for JSON data
    video_blob_url = db.Column(db.String(255), nullable=False)
    contexts = db.Column(db.Text)
