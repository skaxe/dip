from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, SelectField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    team_list1222 = ['Team1', 'Team2', 'Team3', 'Team4']#по идее тянется из БД
    team_list = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton and Hove Albion', 'Burnley', 'Cardiff City', 'Chelsea',
     'Crystal Palace', 'Everton', 'Fulham', 'Huddersfield Town', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City',
      'Manchester United', 'Newcastle United', 'Norwich City', 'Sheffield United', 'Southampton', 'Stoke City',
       'Swansea City', 'Tottenham Hotspur', 'Watford', 'West Bromwich Albion', 'West Ham United', 'Wolverhampton Wanderers']
    team_select1 = SelectField('Выбрать команду 1',choices=team_list, validators=[DataRequired()], option_widget=None, validate_choice=True, render_kw={"class":"custom-select"})
    team_select2 = SelectField('Выбрать команду 2',choices=team_list, validators=[DataRequired()], render_kw={"class":"custom-select"} )
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-primary"})

    