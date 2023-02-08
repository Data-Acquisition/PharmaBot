from application.models import db
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('useradmin.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)
