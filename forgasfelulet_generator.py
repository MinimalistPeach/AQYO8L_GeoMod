import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons 

from objects.sin_curve import SinCurve as Sin
from objects.half_circle_curve import HalfCircleCurve as HalfCircle
from objects.parabolic_curve import ParabolicCurve as Parabolic
from objects.linear_curve import LinearCurve as Linear

def generate_surface(curve_type, scale, offset):
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

# Ábra kirajzolása
fig = plt.figure(figsize=(10, 6))  # Új ábra létrehozása
ax = fig.add_subplot(111, projection='3d')  # 3D tengelyek hozzáadása
plt.subplots_adjust(left=0.3, bottom=0.25)  # Margók beállítása az interaktív elemekhez

# Kiinduló paraméterek
init_curve = Sin()  # Alapértelmezett görbe beállítása (Szinusz görbe)
init_scale = 1.0  # Alapértelmezett skála
init_offset = 1.5  # Alapértelmezett eltolás

# Forgásfelület generálása az alapértelmezett paraméterekkel
X, Y, Z, y_vals = generate_surface(init_curve, init_scale, init_offset)
surface = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='k', linewidth=0.1)  # Forgásfelület kirajzolása

# Tengelyek és cím beállítása
ax.set_xlabel("X")  # X tengely címkéje
ax.set_ylabel("Y")  # Y tengely címkéje
ax.set_zlabel("Z")  # Z tengely címkéje
ax.set_title(f"Forgásfelület - {init_curve.get_name()}")  # Ábra címe a görbe nevével

# A görbe profiljának kiszámítása
f_y = init_curve.calc_profile(init_scale, init_offset, y_vals)
volume = calc_volume(f_y, y_vals)  # Térfogat kiszámítása
surface_area = calc_surface(f_y, y_vals)  # Felszín kiszámítása

# Térfogat és felszín szöveg létrehozása a felületen
volume_display = fig.text(0.1, 0.92, f"Térfogat ≈ {volume:.3f} egység³", fontsize=12, weight="bold", color="darkblue")
surface_display = fig.text(0.1, 0.88, f"Felszín ≈ {surface_area:.3f} egység²", fontsize=12, color="darkgreen", weight="bold")

# Csúszkák definiálása
ax_scale = plt.axes([0.3, 0.15, 0.6, 0.03])  # Skála csúszka helye
ax_offset = plt.axes([0.3, 0.1, 0.6, 0.03])  # Eltolás csúszka helye

slider_scale = Slider(ax_scale, 'Skála', 0.1, 3.0, valinit=init_scale)  # Skála csúszka létrehozása
slider_offset = Slider(ax_offset, 'Eltolás', 0.0, 3.0, valinit=init_offset)  # Eltolás csúszka létrehozása

# Profilgörbe választó rádió gombok létrehozása
ax_radio = plt.axes([0.05, 0.4, 0.2, 0.25])  # Rádió gombok helye
radio = RadioButtons(ax_radio, ['Szinusz', 'Parabolikus', 'Lineáris', 'Félkör'], active=0)  # Rádió gombok definiálása

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

def update(val=None):
    """
    A forgásfelület újragenerálása a felhasználó által megadott paraméterek alapján.

    Parameters:
        val: optional - Beépített paraméter.
    """
    ax.clear()  # Tengelyek törlése az új ábra előtt
    curve_type = get_curve_class(radio.value_selected)  # Kiválasztott görbe osztály lekérése
    scale = slider_scale.val  # Skála értékének lekérése
    offset = slider_offset.val  # Eltolás értékének lekérése

    # Forgásfelület újragenerálása az aktuális paraméterekkel
    X, Y, Z, y_vals = generate_surface(curve_type, scale, offset)
    ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='k', linewidth=0.1)  # Új forgásfelület kirajzolása
    
    # Tengelyek és cím frissítése
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Forgásfelület - {curve_type.get_name()}")

    # Új térfogat és felszín kiszámítása
    f_y = curve_type.calc_profile(scale, offset, y_vals)
    volume = calc_volume(f_y, y_vals)
    surface_area = calc_surface(f_y, y_vals)

    # Térfogat és felszín szöveg frissítése
    volume_display.set_text(f"Térfogat ≈ {volume:.3f} egység³")
    surface_display.set_text(f"Felszín ≈ {surface_area:.3f} egység²")

    fig.canvas.draw_idle()  # Ábra frissítése

# Csúszkák és rádió gombok eseménykezelőinek beállítása
slider_scale.on_changed(update)  # Skála csúszka változásának kezelése
slider_offset.on_changed(update)  # Eltolás csúszka változásának kezelése
radio.on_clicked(update)  # Rádió gomb változásának kezelése

plt.show()  # Ábra megjelenítése