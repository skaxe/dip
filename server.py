from flask import Flask, render_template


from random_predictor import RandomPredictor
app = Flask(__name__)

random_predict = RandomPredictor()

@app.route("/")
def index():

    return_number = str(random_predict.predict())
    print(return_number)
    return render_template('index.html', return_number=return_number)
if __name__ == "__main__":
    app.run()
