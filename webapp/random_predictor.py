import random
from webapp.base_predictor import BasePredictor 


class RandomPredictor(BasePredictor):

    def predict(self):
        number = random.random() 
        return number

