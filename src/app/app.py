#!venv/bin/python
import os
from flask_security.utils import encrypt_password
from application import app, db, PharmaInfo
from flask_ngrok import run_with_ngrok
  # Role, user_datastore


def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    # import string
    # import random

    db.drop_all()
    db.create_all()

    with app.app_context():
      pharma1 = PharmaInfo(name='11111111', address='улица Пушкина')
      pharma2 = PharmaInfo(name='superuser', address='улица тукая', phone='89778684')
      db.session.add(pharma1)
      db.session.add(pharma2)
      db.session.commit()
        # db.session.delete(user_role)
        # db.session.commit()
    
    #     test_user = user_datastore.create_user(
    #         first_name='Admin',
    #         email='admin',
    #         password=encrypt_password('admin'),
    #         roles=[user_role, super_user_role]
    #     )


    #     db.session.commit()
    # return


if __name__ == '__main__':
    app.app_context().push()
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    # database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    # if not os.path.exists(database_path):
    # build_sample_db()

    # Start app
    # run_with_ngrok(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
