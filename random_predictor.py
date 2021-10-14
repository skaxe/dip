import random
from base_predictor import BasePredictor 


class RandomPredictor(BasePredictor):

    def predict(self):
        number = random.random() 
        return number

