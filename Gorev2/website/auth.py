from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Parolanızı yanlış girdiniz lütfen tekrar deneyin.', category='error')
        else:
            flash('Böyle bir email yok.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Böyle bir email zaten var.', category='error')
        elif len(email) < 4:
            flash('Email en az 4 karakterden oluşmalıdır.', category='error')
        elif len(first_name) < 2:
            flash('İsim en az 2 karakterden oluşmalıdır.', category='error')

        elif len(password) < 7:
            flash('Şifre en az 7 karakterden oluşmalıdır.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Hesap oluşturuldu!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
