from . import db
from flask_login import UserMixin
<<<<<<< HEAD
from datetime import datetime
=======
>>>>>>> origin/main

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
<<<<<<< HEAD
    is_instructor = db.Column(db.Boolean, default=False)
=======
>>>>>>> origin/main

class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    patient_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
<<<<<<< HEAD
    complaint = db.Column(db.String(300), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)
    symptoms = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class CaseSolution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    diagnosis = db.Column(db.Text, nullable=False)
    treatment = db.Column(db.Text, nullable=False)
    ai_score = db.Column(db.Float, nullable=True)
    instructor_score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref='solutions')
    case = db.relationship('Case', backref='solutions')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_id = db.Column(db.Integer, db.ForeignKey('case.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    answer_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50), default='general')  # general, physical_exam, lab
    
    case = db.relationship('Case', backref='questions') 
=======
    complaint = db.Column(db.String(300), nullable=False) 
>>>>>>> origin/main
