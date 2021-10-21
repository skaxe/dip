from flask_login import UserMixin
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
#типо база данных

class Team():
    team_list = ['Team1', 'Team2', 'Team3', 'Team4']
    team_list ={'name': 'Team1' ,
    'name': 'Team1' }
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
def __repr__(self):
        return '<User name = {} id ={}'.format(self.username, self.id)