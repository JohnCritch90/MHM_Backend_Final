from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, DateTime, Text, Date, create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(String(255), unique=True, nullable=False)
  email  = db.Column(String(255), unique=True, nullable=False)
  password = db.Column(String(255), unique=True, nullable=False)

  def __repr__(self):
    return f'<User {self.name}>'
  
  def serialize(self):
    return {
      "user_id": self.user_id,
      "username": self.username,
      "email": self.email,
      "password": self.password,
    }
  
class JournalEntries (db.Model):
  __tablename__ = 'journal_entries'
  entry_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer)
  date = db.Column(db.Date, nullable=False)
  mood = db.Column(db.String(255))
  content = db.Column(db.Text)

  def __repr__(self):
    return f'<JournalEntries {self.name}>'

  def serialize(self):
    return {
      "entry_id": self.entry_id,
      "user_id": self.user_id,
      "date": self.date,
      "mood": self.mood,
      "content": self.content,
      "user": self.user
    }
  
class MentalHealthResources (db.Model):
  __tablename__ = 'mental_health_resources'
  resource_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text)
  type = db.Column(db.String(255))
  url = db.Column(db.String(255))

  def __repr__(self):
    return f'<MentalHealthResources {self.name}>'

  def serialize(self):
    return {
      "resource_id": self.resource_id,
      "title": self.title,
      "description": self.description,
      "type": self.type,
      "url": self.url,
    }
  
class MeditationSessions (db.Model):
  __tablename__ = 'meditation_sessions'
  session_id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  duration = db.Column(db.Integer)
  style = db.Column(db.String(255))
  theme = db.Column(db.String(255))
  youtube_url = db.Column(db.String(255))

  def __repr__(self):
    return f'<MeditationSessions {self.name}>'

  def serialize(self):
    return {
      "session_id": self.session_id,
      "title": self.title,
      "duration": self.duration,
      "style": self.style,
      "theme": self.theme,
      "youtube_url": self.youtube_url
    }
  
class SupportGroups (db.Model):
  __tablename__ = 'support_groups'
  group_id  = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  description = db.Column(db.Text)
  meeting_link = db.Column(db.String(255))

  def __repr__(self):
    return f'<SupportGroups {self.name}>'

  def serialize(self):
    return {
      "group_id": self.group_id,
      "title": self.title,
      "description": self.description,
      "meeting_link": self.meeting_link,
      "theme": self.theme
    }
  
  class Notifications (db.Model):
    __tablename__ = 'notifications'
    notification_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(255))
    content = db.Column(db.Text)

    def __repr__(self):
      return f'<Notifications {self.name}>'

    def serialize(self):
      return {
        "notification_id": self.notification_id,
        "user_id": self.user_id,
        "type": self.type,
        "content": self.content,
        "user": self.user
      }