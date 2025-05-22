import time

from modules.calculation import calc_volume, calc_surface
from modules.curve_class import get_curve_class
from modules.initialize import Initialize
from modules.calculation import generate_surface_of_curve
from modules.optimalization import Optimalization

class Drawing:
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

        initialize_module = Initialize()  # Inicializáló modul példányosítása
        fig, ax, radio, slider_scale, slider_offset, volume_display, surface_display = initialize_module.get_attributes() 

        self.optimization_module = Optimalization(initialize_module.init_curve, initialize_module.init_scale, 
                                                        initialize_module.init_offset, initialize_module.X, initialize_module.Y, initialize_module.Z, initialize_module.y_vals)  # Optimalizációs modul példányosítása

        self.fig = fig
        self.ax = ax
        self.radio = radio
        self.slider_scale = slider_scale
        self.slider_offset = slider_offset
        self.volume_display = volume_display
        self.surface_display = surface_display
        self.last_update_time = time.time()  # Utolsó frissítési idő inicializálása

    def update(self, val=None):
        """
        A forgásfelület újragenerálása a felhasználó által megadott paraméterek alapján.

        Parameters:
            val: optional - Beépített paraméter.
        """
        if(time.time() - self.last_update_time < 0.1):  # Ha az utolsó frissítés óta eltelt idő kevesebb mint 0.1 másodperc
            return
        self.last_update_time = time.time()
        
        curve_type = get_curve_class(self.radio.value_selected)  # Kiválasztott görbe osztály lekérése
        scale = self.slider_scale.val  # Skála értékének lekérése
        offset = self.slider_offset.val  # Eltolás értékének lekérése


        if(self.optimization_module.curve_type != curve_type or self.optimization_module.scale != scale or self.optimization_module.offset != offset):  # Ha a görbe típusa megváltozott
        # Forgásfelület újragenerálása az aktuális paraméterekkel
            self.ax.clear()  # Tengelyek törlése
            X, Y, Z, y_vals = generate_surface_of_curve(curve_type, scale, offset)
            self.ax.plot_surface(X, Y, Z, cmap='gray', edgecolor='none', linewidth=0.1)  # Új forgásfelület kirajzolása
            self.optimization_module = Optimalization(curve_type, scale, offset, X, Y, Z, y_vals)  # Optimalizációs modul új példányosítása
        else:
            X, Y, Z, y_vals = self.optimization_module.X, self.optimization_module.Y, self.optimization_module.Z, self.optimization_module.y_vals
            self.ax.plot_surface(X, Y, Z, cmap='gray', edgecolor='none', linewidth=0.1)  # Meglévő forgásfelület kirajzolása

        # Új térfogat és felszín kiszámítása
        f_y = curve_type.calc_profile(scale, offset, y_vals)
        volume = calc_volume(f_y, y_vals)
        surface_area = calc_surface(f_y, y_vals)

        # Tengelyek és cím frissítése
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        self.ax.set_title(f"Forgásfelület - {curve_type.get_name()}")


        # Térfogat és felszín szöveg frissítése
        self.volume_display.set_text(f"Térfogat ≈ {volume:.3f} egység³")
        self.surface_display.set_text(f"Felszín ≈ {surface_area:.3f} egység²")

        self.fig.canvas.draw_idle()  # Ábra frissítése