from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from application.models.user import User
from application.models.notify import Notify
from application.models.pharmainfo import PharmaInfo
from werkzeug.security import generate_password_hash, check_password_hash
from application.maxma import Maxma
from application.models import db
import json
from application.models import *

views = Blueprint('views', __name__)

@views.route('/', methods=['POST'])
# @login_required
def maxma():
    if request.headers['Content-Type'] == 'application/json':
      my_info = json.dumps(request.json)
      print()
      print(my_info)
    # return render_template('map.html', user=current_user)
      return my_info
    
@views.route('/map', methods=['POST', 'GET'])
@login_required
def map():
    return render_template('map.html', user=current_user)

@views.route('/bonus')
@login_required
def bonus():
  person = Maxma(current_user.phone)
  balance = person.get_balance()
  try:
    count_expire_bonus = len(balance.bonuses)
  except:
    count_expire_bonus = None
  # session.permanent = True
  # if 'visits' in session:
  #   session['visits'] = session.get('visits') + 1
  # else:
  #   session['visits'] = 1
  #   session.modified = True
  # return f"<p>Количесвтво баллов = {balance}, количество посещений {session['visits']}"
  return render_template('bonus.html', user=current_user, balance=balance, 
                         count=count_expire_bonus)

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

@views.route('/polls', methods=['GET', 'POST'])
@login_required
def polls():
  polls = PollInfo.query.all()
  return render_template('polls/polls.html', user=current_user, polls=polls)

@views.route('/poll<int:id_poll>', methods=['GET', 'POST'])
@login_required
def poll(id_poll):
  poll = Question.query.filter_by(poll_id=id_poll).all()
  answersList = []
  for question in poll:
    answers = Answer.query.filter_by(question_id=question.id).all()
    answersList.append(answers)
  if request.method == 'POST':
    res = []
    for i in range(1, len(poll) + 1):
      ques = request.form.get(f'q{i}')
      answer = request.form[f'answer{i}']
      res.append({ques: answer})
    print(res)
    return redirect(url_for('views.polls'))
  return render_template('polls/poll.html', user=current_user, poll=poll, answers=answersList)