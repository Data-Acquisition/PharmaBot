from flask import Blueprint, render_template, request, flash, jsonify, session
from flask_login import login_required, current_user
from application.models.notify import Notify
from application.maxma import Maxma
from application.models import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def map():
    return render_template('index.html', user=current_user)
  
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

@views.route('/notify')
@login_required
def nootify():
  if request.method == 'GET':
    note = Notify.query.all()
  return