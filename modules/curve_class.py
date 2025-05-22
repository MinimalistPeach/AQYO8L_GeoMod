from solid_shapes.sin_curve import SinCurve as Sin
from solid_shapes.half_circle_curve import HalfCircleCurve as HalfCircle
from solid_shapes.parabolic_curve import ParabolicCurve as Parabolic
from solid_shapes.linear_curve import LinearCurve as Linear


def get_curve_class(curve_name):
    """
    A kiválasztott görbe nevének megfelelő osztály példányosítása.

    Parameters:
        curve_name: str - A görbe neve (pl. 'Szinusz', 'Parabolikus').

    Returns:
        object: A görbe osztályának példánya.

    Raises:
        ValueError: Ha a görbe neve ismeretlen.
    """
    if curve_name == 'Szinusz':
        return Sin()
    elif curve_name == 'Parabolikus':
        return Parabolic()
    elif curve_name == 'Lineáris':
        return Linear()
    elif curve_name == 'Félkör':
        return HalfCircle()
    else:
        raise ValueError("Ismeretlen görbe típus")  # Hibakezelés ismeretlen görbe esetén