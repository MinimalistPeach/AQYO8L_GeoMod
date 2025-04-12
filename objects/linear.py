from objects.curve import Curve

class Linear(Curve):
    def profile_curve(self, scale, offset, y):
        return scale * y + offset