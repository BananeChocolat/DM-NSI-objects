class Rectangle:
    """définit un rectangle avec les arguments longueur et largeur"""    
    def __init__(self, longueur:float, largeur:float) -> None:
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        """Périmètre : 2*Longueur + 2*Largeur"""
        return self.longueur*2 + self.largeur*2

    def aire(self):
        """Surface : Longueur * Largeur"""
        return self.longueur*self.largeur