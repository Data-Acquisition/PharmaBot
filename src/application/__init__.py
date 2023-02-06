from flask import Flask, url_for, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user
# from flask_security import Security, SQLAlchemyUserDatastore
# import flask_admin
# from flask_admin import helpers as admin_helpers
# from application.views import *
# from application.routes.admin import admin_routing


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from application.models import *
from application.maxma import *
from application.views.auth import auth

app.register_blueprint(auth, url_prefix='/')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.route('/')
@login_required
def hello():
    return render_template('index.html')


@app.route('/cardinfo')
@login_required
def index():
  person = Maxma('f8634ce0-5ca2-4b99-a371-110383cb3ecf', '+79774583897')
  balance = person.get_balance()
  session.permanent = True
  if 'visits' in session:
    session['visits'] = session.get('visits') + 1
  else:
    session['visits'] = 1
    session.modified = True
  return f"<p>Количесвтво баллов = {balance}, количество посещений {session['visits']}"

# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security(app, user_datastore)


# admin = flask_admin.Admin(
#     app,
#     'GENETICO',
#     base_template='my_master.html',
#     template_mode='bootstrap4',
# )



# # admin.add_view(MyModelView(Role, db.session, menu_icon_type='fa',
# #                         menu_icon_value='fa-server', name="Roles"))
# admin.add_view(UserView(User, db.session, menu_icon_type='fa',
#                         menu_icon_value='fa-users', name="Пользователи"))
# admin.add_view(ResearchView(Research, db.session, menu_icon_type='fa',
#                             menu_icon_value='fa-connectdevelop',
#                             name="Исследования и отчёты"))

# @security.context_processor
# def security_context_processor():
#     return dict(
#         admin_base_template=admin.base_template,
#         admin_view=admin.index_view,
#         h=admin_helpers,
#         get_url=url_for
#     )


# app.register_blueprint(admin_routing)
