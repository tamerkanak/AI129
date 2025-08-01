from app import create_app, db
from app.models import User, Case, Question
from werkzeug.security import generate_password_hash

def init_database():
    app = create_app()
    
    with app.app_context():
        # Veritabanını oluştur
        db.create_all()
        print("Veritabanı tabloları oluşturuldu.")
        
        # Test kullanıcıları oluştur
        if not User.query.filter_by(username='student').first():
            student = User(
                username='student',
                password=generate_password_hash('password'),
                is_instructor=False
            )
            db.session.add(student)
            print("Öğrenci kullanıcısı oluşturuldu.")
        
        if not User.query.filter_by(username='instructor').first():
            instructor = User(
                username='instructor',
                password=generate_password_hash('password'),
                is_instructor=True
            )
            db.session.add(instructor)
            print("Eğitmen kullanıcısı oluşturuldu.")
        
        # Test vakaları oluştur
        if not Case.query.first():
            # Vaka 1
            case1 = Case(
                title="Göğüs Ağrısı Vakası",
                patient_name="Mehmet Yılmaz",
                age=45,
                complaint="Göğüs ağrısı ve nefes darlığı",
                medical_history="Hipertansiyon, diyabet",
                symptoms="Göğüs ağrısı, nefes darlığı, terleme"
            )
            db.session.add(case1)
            db.session.flush()  # ID'yi almak için
            
            # Vaka 1 soruları
            questions1 = [
                Question(case_id=case1.id, question_text="Ağrı ne zaman başladı?", answer_text="2 saat önce.", question_type="general"),
                Question(case_id=case1.id, question_text="Ağrının yeri neresi?", answer_text="Göğsün sol tarafı.", question_type="general"),
                Question(case_id=case1.id, question_text="Ağrı hareketle değişiyor mu?", answer_text="Evet, nefes alırken artıyor.", question_type="general"),
                Question(case_id=case1.id, question_text="Tansiyonunuz kaç?", answer_text="160/95 mmHg.", question_type="physical_exam"),
                Question(case_id=case1.id, question_text="Nabzınız kaç?", answer_text="110/dakika.", question_type="physical_exam")
            ]
            for q in questions1:
                db.session.add(q)
            
            # Vaka 2
            case2 = Case(
                title="Karın Ağrısı Vakası",
                patient_name="Fatma Demir",
                age=32,
                complaint="Sağ alt karın ağrısı",
                medical_history="Önceki operasyon yok",
                symptoms="Karın ağrısı, bulantı, iştahsızlık"
            )
            db.session.add(case2)
            db.session.flush()
            
            # Vaka 2 soruları
            questions2 = [
                Question(case_id=case2.id, question_text="Ağrı ne kadar süredir var?", answer_text="12 saat.", question_type="general"),
                Question(case_id=case2.id, question_text="Ağrı sürekli mi?", answer_text="Evet, sürekli.", question_type="general"),
                Question(case_id=case2.id, question_text="Ateşiniz var mı?", answer_text="Evet, 38.5°C.", question_type="physical_exam"),
                Question(case_id=case2.id, question_text="Karın muayenesi nasıl?", answer_text="Sağ alt kadranda hassasiyet var.", question_type="physical_exam"),
                Question(case_id=case2.id, question_text="Bulantı kusma var mı?", answer_text="Evet, 2 kez kustum.", question_type="general")
            ]
            for q in questions2:
                db.session.add(q)
            
            # Vaka 3
            case3 = Case(
                title="Baş Dönmesi Vakası",
                patient_name="Ali Özkan",
                age=58,
                complaint="Baş dönmesi ve denge bozukluğu",
                medical_history="Hipertansiyon, kalp hastalığı",
                symptoms="Baş dönmesi, denge bozukluğu, bulantı"
            )
            db.session.add(case3)
            db.session.flush()
            
            # Vaka 3 soruları
            questions3 = [
                Question(case_id=case3.id, question_text="Baş dönmesi ne zaman başladı?", answer_text="Bu sabah.", question_type="general"),
                Question(case_id=case3.id, question_text="Daha önce böyle bir durum yaşadınız mı?", answer_text="Hayır, ilk defa.", question_type="general"),
                Question(case_id=case3.id, question_text="Görme bozukluğu var mı?", answer_text="Hayır.", question_type="physical_exam"),
                Question(case_id=case3.id, question_text="Konuşma bozukluğu var mı?", answer_text="Hayır.", question_type="physical_exam"),
                Question(case_id=case3.id, question_text="Tansiyonunuz kaç?", answer_text="140/90 mmHg.", question_type="physical_exam")
            ]
            for q in questions3:
                db.session.add(q)
            
            print("Test vakaları oluşturuldu.")
        
        db.session.commit()
        print("Veritabanı başlatma tamamlandı!")
        print("\nTest kullanıcıları:")
        print("- Öğrenci: username='student', password='password'")
        print("- Eğitmen: username='instructor', password='password'")

if __name__ == '__main__':
    init_database() 