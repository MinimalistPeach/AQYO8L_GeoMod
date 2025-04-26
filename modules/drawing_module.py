import numpy as np 
import matplotlib.pyplot as plt

from objects.half_circle_curve import HalfCircleCurve as HalfCircle
from modules.calculation_module import calc_volume, calc_surface
from modules.curve_class_module import get_curve_class
from modules.initialize_module import InitializeModule

class DrawingModule:
    """
    A forgásfelület generálásáért és megjelenítéséért felelős modul.
    """

    def __init__(self):
        """
        Inicializálja a DrawingModule osztályt.

        Parameters:
            fig: matplotlib.figure.Figure - A matplotlib ábra objektum.
            ax: matplotlib.axes._axes.Axes3D - A 3D tengelyek objektuma.
        """

        initialize_module = InitializeModule(self)  # Inicializáló modul példányosítása
        fig, ax, radio, slider_scale, slider_offset, volume_display, surface_display = initialize_module.get_attributes() 

        self.fig = fig
        self.ax = ax
        self.radio = radio
        self.slider_scale = slider_scale
        self.slider_offset = slider_offset
        self.volume_display = volume_display
        self.surface_display = surface_display

    def update(self, val=None):
        """
        A forgásfelület újragenerálása a felhasználó által megadott paraméterek alapján.

        Parameters:
            val: optional - Beépített paraméter.
        """
        self.ax.clear()  # Tengelyek törlése az új ábra előtt
        curve_type = get_curve_class(self.radio.value_selected)  # Kiválasztott görbe osztály lekérése
        scale = self.slider_scale.val  # Skála értékének lekérése
        offset = self.slider_offset.val  # Eltolás értékének lekérése

        # Forgásfelület újragenerálása az aktuális paraméterekkel
        X, Y, Z, y_vals = self.generate_surface(curve_type, scale, offset)
        self.ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='k', linewidth=0.1)  # Új forgásfelület kirajzolása

        # Tengelyek és cím frissítése
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.set_title(f"Forgásfelület - {curve_type.get_name()}")

        # Új térfogat és felszín kiszámítása
        f_y = curve_type.calc_profile(scale, offset, y_vals)
        volume = calc_volume(f_y, y_vals)
        surface_area = calc_surface(f_y, y_vals)

        # Térfogat és felszín szöveg frissítése
        self.volume_display.set_text(f"Térfogat ≈ {volume:.3f} egység³")
        self.surface_display.set_text(f"Felszín ≈ {surface_area:.3f} egység²")

        self.fig.canvas.draw_idle()  # Ábra frissítése


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