from objects.curve import Curve

class Parabolic(Curve):
    def profile_curve(self, scale, offset, y):
        return scale * y**2 + offset