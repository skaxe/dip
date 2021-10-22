from flask import Flask, render_template, flash, redirect, url_for
from webapp.random_predictor import RandomPredictor

from webapp.forms import SubmitForm
from webapp.model import Team
#ЗАПУСК сервера set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

def create_app():
    app = Flask(__name__)
    random_predict = RandomPredictor()
    #form = SubmitForm()
    app.config.from_pyfile('config.py')
    @app.route("/")
    def index():
        submit_form = SubmitForm()
        title = 'Выбор команд'        
        return render_template('index.html', page_title=title,  form=submit_form)

    @app.route('/predict_work', methods=['POST'])
    def predict_work():
        form = SubmitForm()
        title = 'Результат предсказания'
        if form.validate_on_submit():
            return_number = random_predict.predict()
            team1 = form.team_select1.data#Сюда возвращает None -> form.validate_on_submit() не дает зайти в этот блок
            team2 = form.team_select2.data
            if (team1 != team2 and (team1 in form.team_list) and (team2 in form.team_list)):
                return render_template('predict_page.html',form = form, return_number=return_number, page_title=title, team1=team1,team2=team2)
            else:
                return redirect(url_for('index'))
                # надо сделать алерт что команда не та
        flash('Неправильное имя пользователя или пароль')   

        return redirect(url_for('index'))



    # @app.route("/predict")
    # def predict_page():
    #     return_number = str(random_predict.predict())
    #     form = SubmitForm()
    #     title = 'ШАНС НА ПОБЕДУ'
        
             
    #     return redirect(url_for('predict_page'))         
    return app
