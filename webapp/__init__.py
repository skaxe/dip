import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .team_stats.teams import TeamKeys, Team, TEAMS_INFO
from .team_stats.build_bar_plot_with_highlighted_two_teams import build_bar_plot_with_highlighted_two_teams, count_number_of_goals, build_bar_plot_two_teams, aggregate_current_dataframe, extract_plot_values 
import os
import pandas as pd
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
            read_csv_17 = pd.read_csv('webapp/team_stats/stats/17_18.csv')
            read_csv_18 = pd.read_csv('webapp/team_stats/stats/18_19.csv')
            read_csv_19 = pd.read_csv('webapp/team_stats/stats/19_20.csv')
            read_csv_20 = pd.read_csv('webapp/team_stats/stats/20_21.csv')
            read_csv_21 = pd.read_csv('webapp/team_stats/stats/21_22.csv')
            csv_list = [read_csv_17, read_csv_18, read_csv_19, read_csv_20, read_csv_21]
            data = aggregate_current_dataframe(read_csv_21) 
            return_number = random_predict.predict()
            team1 = TeamKeys[form.team_select1.data]
            team2 = TeamKeys[form.team_select2.data]

            build_bar_plot_two_teams(csv_list, team1, team2, plot_name='Количество голов', outname ='webapp/static/images/1.svg', column='goal_score')
            build_bar_plot_two_teams(csv_list, team1, team2, plot_name='Угловые', outname ='webapp/static/images/2.svg', column='corners')
            build_bar_plot_two_teams(csv_list, team1, team2, plot_name='Удары по воротам', outname ='webapp/static/images/3.svg', column='shots_on_goal')
            build_bar_plot_two_teams(csv_list, team1, team2, plot_name='Удары в створ', outname ='webapp/static/images/4.svg', column='shots_on_target')
            build_bar_plot_two_teams(csv_list, team1, team2, plot_name='Желтые карточки', outname ='webapp/static/images/5.svg',  column='yellow_cards')

            build_bar_plot_with_highlighted_two_teams(data, team1, team2, plot_name='Количество голов', outname ='webapp/static/images/Graf1.svg', column='goal_score')
            build_bar_plot_with_highlighted_two_teams(data, team1, team2, plot_name='Угловые', outname ='webapp/static/images/Graf2.svg', column='corners')
            build_bar_plot_with_highlighted_two_teams(data, team1, team2, plot_name='Удары по воротам', outname ='webapp/static/images/Graf3.svg', column='shots_on_goal')
            build_bar_plot_with_highlighted_two_teams(data, team1, team2, plot_name='Удары в створ', outname ='webapp/static/images/Graf4.svg', column='shots_on_target')
            build_bar_plot_with_highlighted_two_teams(data, team1, team2, plot_name='Желтые карточки', outname ='webapp/static/images/Graf5.svg', column='yellow_cards')


            
            team1_pic = f'images/clubs/{team1}.svg'
            team2_pic = f'images/clubs/{team2}.svg'
            if (team1 != team2 ):
                return render_template('predict_page.html',form = form, return_number=return_number, page_title=title, team1=team1,team2=team2, team1_pic=team1_pic, team2_pic=team2_pic)
            else:
                return redirect(url_for('index'))
        

        return redirect(url_for('index'))
    
    return app
