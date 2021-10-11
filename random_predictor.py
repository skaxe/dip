import random
import base_predictor


class Random_predictor(base_predictor.Predictor):    

    def predict(self):
        number = random.random()
        return number
    a = predict(5)
    print(a)
    
