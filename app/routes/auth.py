from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import User
from .. import db, login_manager

bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Hoş geldiniz, {username}!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Kullanıcı adı veya şifre hatalı!', 'error')
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        user_type = request.form.get('user_type', 'student')
        
        # Validasyon
        if not username or not password:
            flash('Kullanıcı adı ve şifre gereklidir!', 'error')
            return render_template('register.html')
        
        if len(username) < 3:
            flash('Kullanıcı adı en az 3 karakter olmalıdır!', 'error')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Şifre en az 6 karakter olmalıdır!', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Şifreler eşleşmiyor!', 'error')
            return render_template('register.html')
        
        # Kullanıcı adı kontrolü
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Bu kullanıcı adı zaten kullanılıyor!', 'error')
            return render_template('register.html')
        
        # Yeni kullanıcı oluştur
        is_instructor = user_type == 'instructor'
        new_user = User(
            username=username,
            password=generate_password_hash(password),
            is_instructor=is_instructor
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash(f'Hesabınız başarıyla oluşturuldu! Hoş geldiniz, {username}!', 'success')
            login_user(new_user)
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash('Kayıt sırasında bir hata oluştu. Lütfen tekrar deneyin.', 'error')
            return render_template('register.html')
    
    return render_template('register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Başarıyla çıkış yaptınız.', 'info')
    return redirect(url_for('auth.login'))

@bp.route('/create_demo_user')
def create_demo_user():
    if not User.query.filter_by(username='demo').first():
        user = User(username='demo', password=generate_password_hash('demo'))
        db.session.add(user)
        db.session.commit()
        return 'Demo kullanıcı oluşturuldu: demo/demo'
    return 'Demo kullanıcı zaten mevcut.' 