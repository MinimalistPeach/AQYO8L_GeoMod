import numpy as np 


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