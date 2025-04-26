from objects.curve import Curve

class ParabolicCurve(Curve):
    """
    Parabolikus görbe osztálya, amely a Curve osztályból származik.
    """
    def calc_profile(self, scale, offset, y):
        """
        Kiszámolja a parabolikus görbe profilját.

        Parameters:
            scale: float - A görbe meredeksége.
            offset: float - A görbe eltolása az y tengely mentén.
            y: numpy.ndarray - Az y koordináták tömbje.

        Returns:
            A parabolikus görbe értékei az adott y koordinátákhoz.
        """
        return scale * y**2 + offset # Parabolikus görbe egyenlete