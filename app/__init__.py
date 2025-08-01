from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    
    # Deployment için veritabanı URI'sini ayarla
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Render/Heroku için PostgreSQL
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Local development için SQLite
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .routes import auth, main, cases
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(cases.bp)

    with app.app_context():
        try:
            db.create_all()
            
            # Örnek veriler ekle (sadece local development'ta)
            if os.environ.get('FLASK_ENV') == 'development' or not os.environ.get('DATABASE_URL'):
                from .models import User, Case, Question
                from werkzeug.security import generate_password_hash
                
                # Eğer kullanıcı yoksa örnek kullanıcılar ekle
                if not User.query.first():
                    student = User(username='student', password=generate_password_hash('123'), is_instructor=False)
                    instructor = User(username='instructor', password=generate_password_hash('123'), is_instructor=True)
                    db.session.add(student)
                    db.session.add(instructor)
                    db.session.commit()
                    
                    # Örnek kullanıcılar için demo vakalar ekle
                    case1 = Case(
                        user_id=student.id,  # student kullanıcısına ait
                        title='Göğüs Ağrısı Vakası',
                        patient_name='Ahmet Yılmaz',
                        age=45,
                        complaint='Göğsümde şiddetli ağrı var, nefes almakta zorlanıyorum',
                        medical_history='Hipertansiyon, diyabet',
                        symptoms='Göğüs ağrısı, nefes darlığı, terleme'
                    )
                    case2 = Case(
                        user_id=student.id,  # student kullanıcısına ait
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
        except Exception as e:
            print(f"Veritabanı başlatma hatası: {e}")
            # Hata durumunda uygulama çalışmaya devam etsin

    return app 