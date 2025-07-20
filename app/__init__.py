<<<<<<< HEAD
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
=======
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
>>>>>>> origin/main
import os

db = SQLAlchemy()
login_manager = LoginManager()

<<<<<<< HEAD
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
=======

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'devkey'
>>>>>>> origin/main
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
<<<<<<< HEAD
    login_manager.login_view = 'auth.login'

    from .routes import auth, main, cases
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(cases.bp)

    with app.app_context():
        db.create_all()
        
        # Örnek veriler ekle
        from .models import User, Case, Question
        from werkzeug.security import generate_password_hash
        
        # Eğer kullanıcı yoksa örnek kullanıcılar ekle
        if not User.query.first():
            student = User(username='student', password=generate_password_hash('123'), is_instructor=False)
            instructor = User(username='instructor', password=generate_password_hash('123'), is_instructor=True)
            db.session.add(student)
            db.session.add(instructor)
            db.session.commit()
        
        # Eğer vaka yoksa örnek vakalar ekle
        if not Case.query.first():
            case1 = Case(
                title='Göğüs Ağrısı Vakası',
                patient_name='Ahmet Yılmaz',
                age=45,
                complaint='Göğsümde şiddetli ağrı var, nefes almakta zorlanıyorum',
                medical_history='Hipertansiyon, diyabet',
                symptoms='Göğüs ağrısı, nefes darlığı, terleme'
            )
            case2 = Case(
                title='Karın Ağrısı Vakası',
                patient_name='Fatma Demir',
                age=32,
                complaint='Karnımın sağ alt kısmında şiddetli ağrı var',
                medical_history='Apendisit ameliyatı geçmişi yok',
                symptoms='Karın ağrısı, bulantı, iştahsızlık'
            )
            db.session.add(case1)
            db.session.add(case2)
            db.session.commit()
            
            # Örnek sorular ekle
            questions1 = [
                Question(case_id=1, question_text='Ağrı ne zaman başladı?', answer_text='2 saat önce aniden başladı.', question_type='general'),
                Question(case_id=1, question_text='Ağrı nereye yayılıyor?', answer_text='Sol kola ve çeneye yayılıyor.', question_type='general'),
                Question(case_id=1, question_text='Daha önce böyle bir ağrı yaşadınız mı?', answer_text='Hayır, ilk defa yaşıyorum.', question_type='general'),
                Question(case_id=1, question_text='Tansiyonunuz kaç?', answer_text='180/110 mmHg.', question_type='physical_exam'),
                Question(case_id=1, question_text='Kalp atış hızınız nedir?', answer_text='110/dakika.', question_type='physical_exam')
            ]
            
            questions2 = [
                Question(case_id=2, question_text='Ağrı ne zaman başladı?', answer_text='Dün gece yarısından itibaren.', question_type='general'),
                Question(case_id=2, question_text='Ağrı sürekli mi yoksa aralıklı mı?', answer_text='Sürekli ve şiddetli.', question_type='general'),
                Question(case_id=2, question_text='Ateşiniz var mı?', answer_text='Evet, 38.5°C.', question_type='physical_exam'),
                Question(case_id=2, question_text='Karnınızda hassasiyet var mı?', answer_text='Evet, sağ alt kadranda çok hassas.', question_type='physical_exam'),
                Question(case_id=2, question_text='Bulantı ve kusma var mı?', answer_text='Bulantı var ama kusma yok.', question_type='general')
            ]
            
            for q in questions1 + questions2:
                db.session.add(q)
            db.session.commit()
=======
    Bootstrap(app)

    from .routes.auth import auth_bp
    from .routes.main import main_bp
    from .routes.cases import cases_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(cases_bp)

    with app.app_context():
        db.create_all()

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404
>>>>>>> origin/main

    return app 