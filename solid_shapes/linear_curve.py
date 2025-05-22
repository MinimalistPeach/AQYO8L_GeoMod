from solid_shapes.curve import Curve

class LinearCurve(Curve):
    """
    Lineáris görbe osztálya, amely a Curve osztályból származik.
    """
    def calc_profile(self, scale, offset, y):
        """
        Kiszámolja a lineáris görbe profilját.

        Parameters:
            scale: float - A görbe meredeksége.
            offset: float - A görbe eltolása az y tengely mentén.
            y: numpy.ndarray - Az y koordináták tömbje.

        Returns:
            A lineáris görbe értékei az adott y koordinátákhoz.
        """
        return scale * y + offset # Lineáris görbe egyenlete