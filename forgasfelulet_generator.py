import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

# Profilgörbék kiszámítása
def profileCurve(y, curve_type, scale=1.0, offset=1.5):
    if curve_type == 'szinusz':
        return scale * np.sin(y) + offset
    elif curve_type == 'parabola':
        return scale * y**2 + offset
    elif curve_type == 'lineáris':
        return scale * y + offset
    elif curve_type == 'félkör':
        return scale * np.sqrt(np.clip(1 - (y - 1)**2, 0, None)) + offset
    else:
        return np.ones_like(y)

# Forgásfelület előállítása
def generateSurface(curve_type, scale, offset):
    y_vals = np.linspace(0, np.pi, 100)
    if curve_type == 'félkör':
        y_vals = np.linspace(0, 2, 100)
    theta_vals = np.linspace(0, 2 * np.pi, 100)
    Y, Theta = np.meshgrid(y_vals, theta_vals)
    
    X_profile = profileCurve(Y, curve_type, scale, offset)
    X = X_profile * np.cos(Theta)
    Z = X_profile * np.sin(Theta)
    return X, Y, Z, y_vals

# Térfogat kiszámítása
def calcVolume(f_y, y_vals):
    return np.pi * np.trapezoid(f_y**2, y_vals)

# Felszín kiszámítása
def calcSurface(f_y, y_vals):
    df_dy = np.gradient(f_y, y_vals)
    integrand = f_y * np.sqrt(1 + df_dy**2)
    return 2 * np.pi * np.trapz(integrand, y_vals)

# Ábra kirajzolása
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.3, bottom=0.25)

# Kiinduló paraméterek
init_curve = 'szinusz'
init_scale = 1.0
init_offset = 1.5

X, Y, Z, y_vals = generateSurface(init_curve, init_scale, init_offset)
surface = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='k', linewidth=0.1)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Forgásfelület - {init_curve}")

f_y = profileCurve(y_vals, init_curve, init_scale, init_offset)
volume = calcVolume(f_y, y_vals)

surface_area = calcSurface(f_y, y_vals)

# Térfogat és felszín szöveg létrehozása
volume_display = fig.text(0.1, 0.92, f"Térfogat ≈ {volume:.3f} egység³", fontsize=12, weight="bold", color="darkblue")

surface_display = fig.text(0.1, 0.88, f"Felszín ≈ {surface_area:.3f} egység²", fontsize=12, color="darkgreen", weight="bold")

# Csúszkák definiálása
ax_scale = plt.axes([0.3, 0.15, 0.6, 0.03])
ax_offset = plt.axes([0.3, 0.1, 0.6, 0.03])

slider_scale = Slider(ax_scale, 'Skála', 0.1, 3.0, valinit=init_scale)
slider_offset = Slider(ax_offset, 'Eltolás', 0.0, 3.0, valinit=init_offset)

# Profilgörbe választó rádió gombok létrehozása
ax_radio = plt.axes([0.05, 0.4, 0.2, 0.25])
radio = RadioButtons(ax_radio, ['szinusz', 'parabola', 'lineáris', 'félkör'], active=0)

# Ábra frissítő eljárás
def update(val=None):
    ax.clear()
    curve_type = radio.value_selected
    scale = slider_scale.val
    offset = slider_offset.val

    X, Y, Z, y_vals = generateSurface(curve_type, scale, offset)
    ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='k', linewidth=0.1)
    
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Forgásfelület - {curve_type}")

    f_y = profileCurve(y_vals, curve_type, scale, offset)
    volume = calcVolume(f_y, y_vals)

    surface_area = calcSurface(f_y, y_vals)

    volume_display.set_text(f"Térfogat ≈ {volume:.3f} egység³")
    surface_display.set_text(f"Felszín ≈ {surface_area:.3f} egység²")

    fig.canvas.draw_idle()

slider_scale.on_changed(update)
slider_offset.on_changed(update)
radio.on_clicked(update)

plt.show()