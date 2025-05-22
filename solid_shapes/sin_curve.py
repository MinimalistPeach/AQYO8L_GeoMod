from solid_shapes.curve import Curve
import numpy as np

class SinCurve(Curve):
    """
    Szinusz görbe osztálya, amely a Curve osztályból származik.
    """
    def calc_profile(self, scale, offset, y):
        """
        Kiszámolja a szinusz görbe profilját.

        Parameters:
            scale: float - A görbe meredeksége.
            offset: float - A görbe eltolása az y tengely mentén.
            y: numpy.ndarray - Az y koordináták tömbje.

        Returns:
            A szinusz görbe értékei az adott y koordinátákhoz.
        """
        return scale * np.sin(y) + offset # Szinusz görbe egyenlete