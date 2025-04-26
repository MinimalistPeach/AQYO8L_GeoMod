import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons 

from objects.sin_curve import SinCurve as Sin
from modules.calculation_module import calc_volume, calc_surface

class InitializeModule:


    def __init__(self, DrawingModule):
        """
        Inicializálja a forgásfelület generálásához szükséges modulokat és elemeket.
        """
         # Ábra kirajzolása
        self.fig = plt.figure(figsize=(10, 6))  # Új ábra létrehozása
        self.ax = self.fig.add_subplot(111, projection='3d')  # 3D tengelyek hozzáadása
        plt.subplots_adjust(left=0.3, bottom=0.25)  # Margók beállítása az interaktív elemekhez
        # Kiinduló paraméterek
        self.init_curve = Sin()  # Alapértelmezett görbe beállítása (Szinusz görbe)
        self.init_scale = 1.0  # Alapértelmezett skála
        self.init_offset = 1.5  # Alapértelmezett eltolás
        # Forgásfelület generálása az alapértelmezett paraméterekkel
        X, Y, Z, y_vals = DrawingModule.generate_surface(self.init_curve, self.init_scale, self.init_offset)
        self.surface = self.ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='k', linewidth=0.1)  # Forgásfelület kirajzolása

        # Tengelyek és cím beállítása
        self.ax.set_xlabel("X")  # X tengely címkéje
        self.ax.set_ylabel("Y")  # Y tengely címkéje
        self.ax.set_zlabel("Z")  # Z tengely címkéje
        self.ax.set_title(f"Forgásfelület - {self.init_curve.get_name()}")  # Ábra címe a görbe nevével

        # A görbe profiljának kiszámítása
        f_y = self.init_curve.calc_profile(self.init_scale, self.init_offset, y_vals)
        self.volume = calc_volume(f_y, y_vals)  # Térfogat kiszámítása
        self.surface_area = calc_surface(f_y, y_vals)  # Felszín kiszámítása

        # Térfogat és felszín szöveg létrehozása a felületen
        self.volume_display = self.fig.text(0.1, 0.92, f"Térfogat ≈ {self.volume:.3f} egység³", fontsize=12, weight="bold", color="darkblue")
        self.surface_display = self.fig.text(0.1, 0.88, f"Felszín ≈ {self.surface_area:.3f} egység²", fontsize=12, color="darkgreen", weight="bold")

        # Csúszkák definiálása
        self.ax_scale = plt.axes([0.3, 0.15, 0.6, 0.03])  # Skála csúszka helye
        self.ax_offset = plt.axes([0.3, 0.1, 0.6, 0.03])  # Eltolás csúszka helye

        self.slider_scale = Slider(self.ax_scale, 'Skála', 0.1, 3.0, valinit=self.init_scale)  # Skála csúszka létrehozása
        self.slider_offset = Slider(self.ax_offset, 'Eltolás', 0.0, 3.0, valinit=self.init_offset)  # Eltolás csúszka létrehozása

        # Profilgörbe választó rádió gombok létrehozása
        self.ax_radio = plt.axes([0.05, 0.4, 0.2, 0.25])  # Rádió gombok helye
        self.radio = RadioButtons(self.ax_radio, ['Szinusz', 'Parabolikus', 'Lineáris', 'Félkör'], active=0)  # Rádió gombok definiálása


    def get_attributes(self):
        """
        Visszaadja a modul attribútumait.

        Returns:
            tuple: A modul attribútumai (fig, ax, radio, slider_scale, slider_offset, volume_display, surface_display).
        """
        return self.fig, self.ax, self.radio, self.slider_scale, self.slider_offset, self.volume_display, self.surface_display
