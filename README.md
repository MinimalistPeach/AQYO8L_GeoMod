# Geometriai modellezés tárgyhoz készül repository
## Forgásfelület generátor

Ez a beadandó egy interaktív, paraméterezhető **forgásfelület generátort** tartalmaz, amely lehetővé teszi különféle görbék körbeforgatásából keletkező 3D felületek vizuális megjelenítését.


---

### Funkciók

- Interaktív csúszkák:
  - **Skála** (a görbe függőleges nyújtása)
  - **Eltolás** (a görbe vízszintes mozgatása)
- Profilgörbe választás:
  - `szinusz`
  - `parabola`
  - `lineáris`
  - `félkör`
- 3D forgásfelület megjelenítés valós idejű újrarendereléssel
- Egyszerű grafikus felület `matplotlib.widgets` használatával
- Kirajzolt test térfogatának és felszínének kiszámítása

---


### Elvégezhető vizsgálatok

    - Test forma változás megfigyelés a profilgörbe módosításával

    - Görbe megnyúlásának vizsgálata a skálázás változtatásával

    - A test körkörös nagyítása és kicsinyítése az eltolás változtatásával

---

### Követelmények

- Python 3.X
- `numpy`
- `matplotlib`

#### Telepítés:

```bash
pip install -r requirements.txt
```
vagy:
```bash
.\install_deps.bat
```

### Használat
A függőségek telepítése után futtassuk a python fájlt:
```bash
python forgasfelulet_generator.py
```

### Windows hosszú név hiba
Ha a függőségek feltelepítése közben hiba lép fel, akkor nagy valószínűséggel a Windows hosszú fájlnév letiltott funkciójához lehet köze. Ezt az alábbi linken leírtak szerint lehet javítani:
[Windows hosszú fájlnév hiba javítása](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later)


