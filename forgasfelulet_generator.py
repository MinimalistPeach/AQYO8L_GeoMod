import matplotlib.pyplot as plt

from modules.drawing_module import DrawingModule


 # Attribútumok lekérése
drawing_module = DrawingModule()  # Kirajzoló modul példányosítása


# Csúszkák és rádió gombok eseménykezelőinek beállítása
drawing_module.slider_scale.on_changed(drawing_module.update)  # Skála csúszka változásának kezelése
drawing_module.slider_offset.on_changed(drawing_module.update)  # Eltolás csúszka változásának kezelése
drawing_module.radio.on_clicked(drawing_module.update)  # Rádió gomb változásának kezelése

plt.show()  # Ábra megjelenítése