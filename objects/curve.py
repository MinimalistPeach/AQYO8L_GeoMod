import numpy as np

class Curve:
    def profile_curve(self, scale, offset, y):
        return np.ones_like(y)
    
    def get_name(self):
        return self.__class__.__name__.lower()