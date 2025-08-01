from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import Case
from .. import db

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    # Kullanıcının sadece kendi vakalarını göster
    cases = Case.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', cases=cases)

@bp.route('/add_demo_cases')
@login_required
def add_demo_cases():
    # Kullanıcının kendi demo vakalarını ekle
    if not Case.query.filter_by(user_id=current_user.id).first():
        demo_cases = [
            Case(
                user_id=current_user.id,
                title='Akut Apandisit', 
                patient_name='Ali Yılmaz', 
                age=24, 
                complaint='Sağ alt kadranda ağrı ve bulantı'
            ),
            Case(
                user_id=current_user.id,
                title='Hipertansiyon', 
                patient_name='Ayşe Demir', 
                age=56, 
                complaint='Baş ağrısı ve yüksek tansiyon'
            ),
            Case(
                user_id=current_user.id,
                title='Diyabetik Ayak', 
                patient_name='Mehmet Kaya', 
                age=65, 
                complaint='Ayakta yara ve enfeksiyon'
            ),
            Case(
                user_id=current_user.id,
                title='Astım Atağı', 
                patient_name='Zeynep Koç', 
                age=18, 
                complaint='Nefes darlığı ve öksürük'
            )
        ]
        db.session.add_all(demo_cases)
        db.session.commit()
        return 'Demo vakalar eklendi!'
    return 'Zaten vakalar mevcut.' 