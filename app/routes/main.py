from flask import Blueprint, render_template
from flask_login import login_required
from ..models import Case
from .. import db

<<<<<<< HEAD
bp = Blueprint('main', __name__)

@bp.route('/')
=======
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
>>>>>>> origin/main
@login_required
def index():
    cases = Case.query.all()
    return render_template('index.html', cases=cases)

<<<<<<< HEAD
@bp.route('/add_demo_cases')
=======
@main_bp.route('/add_demo_cases')
>>>>>>> origin/main
def add_demo_cases():
    if not Case.query.first():
        demo_cases = [
            Case(title='Akut Apandisit', patient_name='Ali Yılmaz', age=24, complaint='Sağ alt kadranda ağrı ve bulantı'),
            Case(title='Hipertansiyon', patient_name='Ayşe Demir', age=56, complaint='Baş ağrısı ve yüksek tansiyon'),
            Case(title='Diyabetik Ayak', patient_name='Mehmet Kaya', age=65, complaint='Ayakta yara ve enfeksiyon'),
            Case(title='Astım Atağı', patient_name='Zeynep Koç', age=18, complaint='Nefes darlığı ve öksürük')
        ]
        db.session.add_all(demo_cases)
        db.session.commit()
        return 'Demo vakalar eklendi!'
    return 'Zaten vakalar mevcut.' 