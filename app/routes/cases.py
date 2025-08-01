from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Case, Question, CaseSolution, User
from ..ai_service import ai_service
from .. import db

bp = Blueprint('cases', __name__)

@bp.route('/case/<int:case_id>')
@login_required
def case_detail(case_id):
    case = Case.query.get_or_404(case_id)
    questions = Question.query.filter_by(case_id=case_id).all()
    return render_template('case_detail.html', case=case, questions=questions)

@bp.route('/case/<int:case_id>/ask_question', methods=['POST'])
@login_required
def ask_question(case_id):
    case = Case.query.get_or_404(case_id)
    question_text = request.form.get('question')
    
    if not question_text:
        flash('Lütfen bir soru girin.', 'error')
        return redirect(url_for('cases.case_detail', case_id=case_id))
    
    # AI'dan dinamik cevap al
    case_context = f"Hasta: {case.patient_name}, Yaş: {case.age}, Şikayet: {case.complaint}"
    answer = ai_service.generate_dynamic_answer(question_text, case_context)
    
    # Yeni soru ve cevabı veritabanına kaydet
    new_question = Question(
        case_id=case_id,
        question_text=question_text,
        answer_text=answer,
        question_type='dynamic'
    )
    db.session.add(new_question)
    db.session.commit()
    
    flash('Soru soruldu ve cevap alındı.', 'success')
    return redirect(url_for('cases.case_detail', case_id=case_id))

@bp.route('/case/<int:case_id>/solve', methods=['GET', 'POST'])
@login_required
def solve_case(case_id):
    case = Case.query.get_or_404(case_id)
    
    if request.method == 'POST':
        diagnosis = request.form.get('diagnosis')
        treatment = request.form.get('treatment')
        
        if not diagnosis or not treatment:
            flash('Lütfen hem tanı hem de tedavi önerinizi girin.', 'error')
            return render_template('solve_case.html', case=case)
        
        # AI değerlendirmesi al
        case_info = {
            'patient_name': case.patient_name,
            'age': case.age,
            'complaint': case.complaint,
            'medical_history': case.medical_history,
            'symptoms': case.symptoms
        }
        
        evaluation = ai_service.evaluate_solution(case_info, diagnosis, treatment)
        
        # Çözümü veritabanına kaydet
        solution = CaseSolution(
            user_id=current_user.id,
            case_id=case_id,
            diagnosis=diagnosis,
            treatment=treatment,
            ai_score=evaluation.get('score', 0)
        )
        db.session.add(solution)
        db.session.commit()
        
        flash('Vaka çözümünüz kaydedildi ve değerlendirildi.', 'success')
        return render_template('solution_result.html', 
                             case=case, 
                             solution=solution, 
                             evaluation=evaluation)
    
    return render_template('solve_case.html', case=case)

@bp.route('/generate_case', methods=['GET', 'POST'])
@login_required
def generate_case():
    if request.method == 'POST':
        difficulty = request.form.get('difficulty', 'medium')
        specialty = request.form.get('specialty', 'general')
        
        # AI ile yeni vaka oluştur
        case_data = ai_service.generate_case(difficulty, specialty)
        
        # Vakayı veritabanına kaydet
        new_case = Case(
            title=case_data['title'],
            patient_name=case_data['patient_name'],
            age=case_data['age'],
            complaint=case_data['complaint'],
            medical_history=case_data.get('medical_history', ''),
            symptoms=case_data.get('symptoms', '')
        )
        db.session.add(new_case)
        db.session.commit()
        
        # Soruları kaydet
        for q_data in case_data.get('questions', []):
            question = Question(
                case_id=new_case.id,
                question_text=q_data['question'],
                answer_text=q_data['answer'],
                question_type=q_data.get('type', 'general')
            )
            db.session.add(question)
        
        db.session.commit()
        flash('Yeni vaka başarıyla oluşturuldu!', 'success')
        return redirect(url_for('cases.case_detail', case_id=new_case.id))
    
    return render_template('generate_case.html')

# Eğitmen paneli - Öğrenci çözümlerini listeleme (US09)
@bp.route('/instructor/solutions')
@login_required
def instructor_solutions():
    if not current_user.is_instructor:
        flash('Bu sayfaya erişim yetkiniz yok.', 'error')
        return redirect(url_for('main.index'))
    
    # Tüm öğrenci çözümlerini getir
    solutions = CaseSolution.query.join(User).join(Case).order_by(CaseSolution.created_at.desc()).all()
    return render_template('instructor_solutions.html', solutions=solutions)

# Eğitmen puanlama sistemi (US10)
@bp.route('/instructor/solution/<int:solution_id>/grade', methods=['GET', 'POST'])
@login_required
def grade_solution(solution_id):
    if not current_user.is_instructor:
        flash('Bu sayfaya erişim yetkiniz yok.', 'error')
        return redirect(url_for('main.index'))
    
    solution = CaseSolution.query.get_or_404(solution_id)
    
    if request.method == 'POST':
        instructor_score = request.form.get('instructor_score')
        instructor_comment = request.form.get('instructor_comment', '')
        
        if instructor_score:
            try:
                score = float(instructor_score)
                if 0 <= score <= 100:
                    solution.instructor_score = score
                    # Eğitmen yorumunu kaydetmek için yeni bir alan eklenebilir
                    db.session.commit()
                    flash('Puanlama başarıyla kaydedildi.', 'success')
                    return redirect(url_for('cases.instructor_solutions'))
                else:
                    flash('Puan 0-100 arasında olmalıdır.', 'error')
            except ValueError:
                flash('Geçerli bir puan giriniz.', 'error')
        else:
            flash('Lütfen bir puan giriniz.', 'error')
    
    return render_template('grade_solution.html', solution=solution)

# Kullanıcı geçmiş çözümlerini görme (US15)
@bp.route('/my-solutions')
@login_required
def my_solutions():
    # Kullanıcının kendi çözümlerini getir
    solutions = CaseSolution.query.filter_by(user_id=current_user.id).join(Case).order_by(CaseSolution.created_at.desc()).all()
    return render_template('my_solutions.html', solutions=solutions)
