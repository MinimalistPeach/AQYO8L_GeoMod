import objects.sin_curve as Sin

class OptimalizationModule:
    def __init__(self, curve_type, scale, offset, X, Y, Z, y_vals):
        """
        Inicializálja az optimalizációs modult.
        """
        self.curve_type = curve_type
        self.scale = scale
        self.offset = offset
        self.X = X
        self.Y = Y
        self.Z = Z
        self.y_vals = y_vals