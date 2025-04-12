from objects.curve import Curve
import numpy as np

class HalfCircle(Curve):
    def profile_curve(self, scale, offset, y):
        return scale * np.sqrt(np.clip(1 - (y - 1)**2, 0, None)) + offset