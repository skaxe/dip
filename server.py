from flask import Flask, render_template


from random_predictor import Random_predictor
app = Flask(__name__)

@app.route("/")
def index():

    title = 'Случайное число'
    lol = 0.124124124
    
    return_number = str(Random_predictor.predict(5))
    return render_template('index.html',page_title = title, return_number = return_number)
if __name__=="__main__":
    app.run()
