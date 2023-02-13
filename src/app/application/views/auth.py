from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from application.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import db  ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from application.maxma import Maxma


auth = Blueprint('auth', __name__)

@auth.route('/loginphone', methods=['GET', 'POST'])
def login_phone():
  if request.method == 'POST':
    phone = request.form.get('phone')
    user = User.query.filter_by(phone=phone).first()
    if user:
      flash(f'Введите пароль', category='success')
      session['phone'] = phone
      return redirect(url_for('auth.login_password'))
    else:
      flash('Пройдите регистрацию', category='error')
      
  return render_template("login_phone.html", user=current_user)

@auth.route('/loginpassword', methods=['GET', 'POST'])
def login_password():
  if request.method == 'POST':
    phone = session['phone']
    password = request.form.get('password')
    user = User.query.filter_by(phone=phone).first()
    if check_password_hash(user.password, password):
      flash(f'Logged in successfully!', category='success')
      login_user(user, remember=True)
      return redirect(url_for('views.notify'))
    else:
      flash(f'Incorrect password, try again.', category='error')
      
  return render_template("login_password.html", user=current_user)



# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         phone = request.form.get('phone')
#         password = request.form.get('password')

#         user = User.query.filter_by(phone=phone).first()
#         person = Maxma(phone)
#         if user:
#             if check_password_hash(user.password, password):
#                 flash(f'Logged in successfully! {person.get_balance().client.bonuses}', category='success')
#                 login_user(user, remember=True)
#                 return redirect(url_for('views.map'))
#             else:
#                 flash(f'Incorrect password, try again.', category='error')
#         else:
#             flash(f'phone does not exist.', category='error')

#     return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login_phone'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        phone = request.form.get('phone')
        session['phone'] = phone
        email = request.form.get('email')
        birthdate = request.form.get('birthdate')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(phone=phone).first()
        if user:
            flash('phone already exists.', category='error')
        # elif len(email) < 4:
        #     flash('Email must be greater than 3 characters.', category='error')
        # elif len(first_name) < 2:
        #     flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        # elif len(password1) < 7:
        #     flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(phone=phone, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            client = Maxma(phone)
            client.add_new_client_short(phone, email, first_name, birthdate)
            flash('Account created!', category='success')
            return redirect(url_for('views.notify'))

    return render_template("sign_up.html", user=current_user)