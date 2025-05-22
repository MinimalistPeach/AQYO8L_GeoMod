import numpy as np

class Curve:
    """Görbe ősosztály"""
    def calc_profile(self, scale, offset, y):
        """
        Görbe profiljának kiszámítása.
        """
        return np.ones_like(y)
    
    def get_name(self):
        """
        Görbe nevének visszaadása magyarra fordítva.

        Parameters:
            None
        
        Returns:
            str: A görbe neve magyarul.
        """
        translations = {
            'sin': 'Szinusz', # Osztály nevek magyar megfelelői
            'parabolic': 'Parabolikus',
            'linear': 'Lineáris',
            'halfcircle': 'Félkör',
        }
        name = self.__class__.__name__.lower().replace('curve', '') # Osztály névből curve szó eltávolítása
        formatted_name = ' '.join(word.capitalize() for word in name.split()) # Osztály név kezdőbetűjének kapitalizálása
        return translations.get(name, formatted_name) # Görbe nevének visszaadása magyar megfelelővel, ha van