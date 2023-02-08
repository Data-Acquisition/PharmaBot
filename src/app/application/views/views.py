from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
from application.models.user import User
from application.models.notify import Notify
from application.models.pharmainfo import PharmaInfo
from werkzeug.security import generate_password_hash, check_password_hash
from application.maxma import Maxma
from application.models import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def map():
    return render_template('map.html', user=current_user)
  
@views.route('/bonus')
@login_required
def bonus():
  person = Maxma(current_user.phone)
  balance = person.get_balance()
  # session.permanent = True
  # if 'visits' in session:
  #   session['visits'] = session.get('visits') + 1
  # else:
  #   session['visits'] = 1
  #   session.modified = True
  # return f"<p>Количесвтво баллов = {balance}, количество посещений {session['visits']}"
  return render_template('bonus.html', user=current_user, balance=balance)

@views.route('/help')
@login_required
def help():
  return render_template('help.html', user=current_user)

@views.route('/notify', methods=['GET', 'POST'])
@login_required
def notify():
  if request.method == 'GET':
    notes = Notify.query.all()
  return render_template('notify.html', notes=notes, user=current_user)

@views.route('/pharma', methods=['GET', 'POST'])
@login_required
def pharma():
  if request.method == 'GET':
    pharmacies = PharmaInfo.query.all()
  return render_template('pharmainfo.html', pharmacies=pharmacies, user=current_user)

@views.route('/feedback')
@login_required
def feedback():
  return render_template('feedback.html', user=current_user)

@views.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
  if request.method == 'POST':
    phone = request.form.get('phone')
    password = request.form.get('password')
    user = User.query.filter_by(phone=session['phone']).first()
    if phone:
      client = Maxma(session['phone'])
      client.update_client(phone) 
      user.phone = phone
      session['phone'] = phone
      db.session.commit() 
      flash('Телефон успешно изменён!', category='success')
    if password:
      user.password = generate_password_hash(password, method='sha256')
      db.session.commit()  
      flash('Пароль успешно изменён!', category='success')
  return render_template('settings/settings.html', user=current_user)