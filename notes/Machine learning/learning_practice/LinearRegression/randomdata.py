import numpy as np  
class RandomData():
    def __init__(self):
        self.n_samples = 100 # Number of data points
        np.random.seed(0)
        self.data = np.random.randn(100)

    def function(self, X):
        return 0.5*X + 1
    
    def generate_data(self):
        x_train = np.sort(np.random.rand(self.n_samples) ) 
        y_train = (self.function(x_train) + np.random.randn(self.n_samples) * 0.05).reshape(self.n_samples, 1)
        return x_train.reshape(self.n_samples, 1), y_train
