from flask import Flask, render_template, flash, redirect, url_for
from forms import SubmitForm

from random_predictor import RandomPredictor
from model import Team
app = Flask(__name__)

random_predict = RandomPredictor()
app.config.from_pyfile('config.py')

@app.route("/")
def index():
    title = 'Выбор команд'
    submit_form = SubmitForm()
    return render_template('index.html', form=submit_form, page_title=title) 

@app.route("/predict", methods=['POST'])
def predict_page():
    return_number = str(random_predict.predict())
    form = SubmitForm()
    title = 'ШАНС НА ПОБЕДУ'
    
    if form.validate_on_submit(): 
        team1 = form.team_select1.data#Сюда возвращает None -> form.validate_on_submit() не дает зайти в этот блок
        team2 = form.team_select2.data
        if (team1 != team2 and (team1 in form.team_list) and (team2 in form.team_list)):
            return render_template('predict_page.html',form = form, return_number=return_number, page_title=title)
        else:
            return redirect(url_for('index'))# надо сделать алерт
    flash('Неправильное имя пользователя или пароль')        
    return redirect(url_for('index'))         
       

if __name__ == "__main__":
    app.run()
