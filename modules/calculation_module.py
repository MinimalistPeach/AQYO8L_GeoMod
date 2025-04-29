import numpy as np 

from objects.half_circle_curve import HalfCircleCurve as HalfCircle


def calc_volume(f_y, y_vals):
    """
    Térfogat kiszámítása a forgásfelület görbéjének integrálásával.

    Parameters:
        f_y: numpy.ndarray - A görbe profiljának értékei.
        y_vals: numpy.ndarray - Az y tengely mentén vett értékek.

    Returns:
        float: A forgásfelület térfogata.
    """
    return np.pi * np.trapezoid(f_y**2, y_vals)

def calc_surface(f_y, y_vals):
    """
    Felszín kiszámítása a görbe deriváltjának és profiljának felhasználásával.

    Parameters:
        f_y: numpy.ndarray - A görbe profiljának értékei.
        y_vals: numpy.ndarray - Az y tengely mentén vett értékek.

    Returns:
        float: A forgásfelület felszíne.
    """
    df_dy = np.gradient(f_y, y_vals)
    # Felszín integráljának kiszámítása
    integrand = f_y * np.sqrt(1 + df_dy**2)
    return 2 * np.pi * np.trapz(integrand, y_vals)


def generate_surface_of_curve(curve_type, scale, offset):
    """
    Forgásfelület előállítása a megadott görbe típus, skála és eltolás alapján.

    Parameters:
        curve_type: Az aktuális görbe osztálya (pl. Sin, Parabolic, stb.).
        scale: float - A görbe skálázási tényezője.
        offset: float - A görbe eltolási értéke.

    Returns:
        tuple: Forgásfelület koordinátái (X, Y, Z) és az y értékek (y_vals).
    """
    y_vals = np.linspace(0, np.pi, 100)  # Alapértelmezett y értékek előállítása
    if isinstance(curve_type, HalfCircle):  # Ha a görbe félkör, más tartományt használunk
        y_vals = np.linspace(0, 2, 100)
    theta_vals = np.linspace(0, 2 * np.pi, 100)  # Forgásszög értékek generálása
    Y, Theta = np.meshgrid(y_vals, theta_vals)  # Rács generálása a forgáshoz

    # A görbe profiljának kiszámítása a megadott skála és eltolás alapján
    X_profile = curve_type.calc_profile(scale, offset, Y)
    X = X_profile * np.cos(Theta)  # Forgatás X koordinátája
    Z = X_profile * np.sin(Theta)  # Forgatás Z koordinátája
    return X, Y, Z, y_vals  # Forgásfelület koordinátáinak visszaadása