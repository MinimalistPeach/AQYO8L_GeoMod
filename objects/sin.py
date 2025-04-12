from objects.curve import Curve
import numpy as np

class Sin(Curve):
    def profile_curve(self, scale, offset, y):
        return scale * np.sin(y) + offset