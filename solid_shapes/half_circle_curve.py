from solid_shapes.curve import Curve
import numpy as np

class HalfCircleCurve(Curve):
    """
    Félkör görbe osztálya, amely a Curve osztályból származik.
    """
    def calc_profile(self, scale, offset, y):
        """
        Kiszámolja a félkör görbe profilját.

        Parameters:
            scale: float - A görbe meredeksége.
            offset: float - A görbe eltolása az y tengely mentén.
            y: numpy.ndarray - Az y koordináták tömbje.

        Returns:
            A félkör görbe értékei az adott y koordinátákhoz.
        """
        return scale * np.sqrt(np.clip(1 - (y - 1)**2, 0, None)) + offset # Félkör görbe egyenlete