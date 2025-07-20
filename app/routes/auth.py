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