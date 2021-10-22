from flask_login import UserMixin
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
#типо база данных не подключается может проблема в этом

class Team():
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
def __repr__(self):
        return '<User name = {} id ={}'.format(self.username, self.id)