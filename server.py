from flask import Flask, render_template


from random_predictor import RandomPredictor
app = Flask(__name__)

random_predict = RandomPredictor()

@app.route("/")
def index():

    return_number = str(random_predict.predict())
    print(return_number)
    team_list = ['Team1', 'Team2', 'Team3', 'Team4']
    return render_template('index.html', return_number=return_number, team_list = team_list)
if __name__ == "__main__":
    app.run()
